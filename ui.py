import bpy

class VIEW3D_PT_TextureCycle(bpy.types.Panel):
    """Creates a Panel in the 3D Viewport Sidebar"""
    bl_label = "Shader Cycle"
    bl_idname = "VIEW3D_PT_texture_cycle"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Texture Cycle' # This is the name of the vertical tab on the sidebar

    def draw(self, context):
        layout = self.layout
        scene = context.scene.texture_cycle_data
        
        col = layout.column(align=True)
        col.label(text="Cycle Actions:")
        
        if not scene.is_cycled:
            col.operator("texture_cycle.cycle_mats", text="Cycle to Diagnostic", icon='NODE_MATERIAL')
        else:
            col.operator("texture_cycle.restore_mats", text="Restore Originals", icon='LOOP_BACK')

        layout.separator()
        
        # UI for settings (Toggles)
        box = layout.box()
        box.label(text="Settings", icon='SETTINGS')
        box.prop(scene, "is_cycled", text="Currently Cycled")
