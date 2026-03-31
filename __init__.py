bl_info = {
    "name": "Blender Texture Cycle",
    "author": "Maximus C Nichol",
    "version": (0, 1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Sidebar > Texture Cycle",
    "description": "Non-destructively cycle materials to a diagnostic shader.",
    "category": "Material",
}

import bpy

from . import properties, operators, ui, utils

classes = (
    properties.MaterialBackup,
    properties.TextureCycleProperties,
    operators.OT_CycleTextures,
    operators.OT_RestoreTextures,
    ui.VIEW3D_PT_TextureCycle,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.texture_cycle_data = bpy.props.PointerProperty(
        type=properties.TextureCycleProperties
    )

def unregister():

    del bpy.types.Scene.texture_cycle_data
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
