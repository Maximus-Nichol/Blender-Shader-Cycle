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
        self.report({'INFO'}, "NOT IMPLEMENTED")
        return {'FINISHED'}
