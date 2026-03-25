import bpy

class OT_CycleTextures(bpy.types.Operator):
    bl_idname = "texture_cycle.cycle_mats"
    bl_label = "Cycle Materials"
    
    def execute(self, context):
        self.report({'INFO'}, "NOT IMPLEMENTED")
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
