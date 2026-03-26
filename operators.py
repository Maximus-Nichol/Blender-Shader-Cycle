import bpy

class OT_CycleTextures(bpy.types.Operator):
    bl_idname = "texture_cycle.cycle_mats"
    bl_label = "Cycle Materials"
    
    def execute(self, context):
        props = context.scene.texture_cycle_data
        props.backup_data.clear() # Start fresh
        
        # Iterate over all materials in the file
        for mat in bpy.data.materials:
            # Filter: Only process materials being used and that use nodes
            if mat.users > 0 and mat.use_nodes:
                
                output_node = utils.find_output_node(mat)
                if not output_node:
                    continue
                
                surface_input = output_node.inputs['Surface']
                
                # Check if something is actually plugged into the Surface
                if surface_input.is_linked:
                    original_link = surface_input.links[0]
                    original_node = original_link.from_node
                    
                    # 1. Save state to our CollectionProperty
                    item = props.backup_data.add()
                    item.material_name = mat.name
                    item.original_node_name = original_node.name
                    
                    # 2. Get the color using your utility
                    extracted_color = utils.get_node_color(original_node)
                    
                    # 3. Create the Diagnostic Shader (Emission is great for this)
                    nodes = mat.node_tree.nodes
                    diag_node = nodes.new(type='ShaderNodeEmission')
                    diag_node.name = "TC_DIAGNOSTIC"
                    diag_node.label = "Diagnostic Mode"
                    diag_node.inputs['Color'].default_value = extracted_color
                    
                    # 4. Re-link: New Node -> Material Output
                    mat.node_tree.links.new(diag_node.outputs[0], surface_input)

        props.is_cycled = True
        self.report({'INFO'}, f"Cycled {len(props.backup_data)} materials.")
        return {'FINISHED'}

class OT_RestoreTextures(bpy.types.Operator):
    bl_idname = "texture_cycle.restore_mats"
    bl_label = "Restore Materials"
    
    def execute(self, context):
        props = context.scene.texture_cycle_data
        
        # Iterate through the stored backup list
        for entry in props.backup_data:
            mat = bpy.data.materials.get(entry.material_name)
            if not mat or not mat.use_nodes:
                continue
            
            tree = mat.node_tree
            output_node = utils.find_output_node(mat)
            if not output_node:
                continue
                
            # Finds the original node from storage
            original_node = tree.nodes.get(entry.original_node_name)
            
            diag_node = None
            if output_node.inputs['Surface'].is_linked:
                diag_node = output_node.inputs['Surface'].links[0].from_node
            
            # Reconnects the original node
            if original_node:
                # Assumes the shader output is index 0 
                # (Standard for BSDFs and Groups)
                tree.links.new(original_node.outputs[0], output_node.inputs['Surface'])
            
            if diag_node and diag_node.name.startswith("TC_DIAG"):
                tree.nodes.remove(diag_node)

        props.backup_data.clear()
        props.is_cycled = False
        
        self.report({'INFO'}, "Original materials restored.")
        return {'FINISHED'}{'FINISHED'}
