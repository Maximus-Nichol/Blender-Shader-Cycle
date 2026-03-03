bl_info = {
    "name": "Blender Texture Cycle",
    "author": "Maximus C Nichol",
    "version": (0, 1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Sidebar > Texture Cycle",
    "description": "Non-destructively cycle materials to a diagnostic shader.",
    "category": "Material",
}

# 1. Import your sub-modules
if "bpy" in locals():
    import importlib
    importlib.reload(properties)
    importlib.reload(operators)
    importlib.reload(ui)
    importlib.reload(utils)
else:
    from . import properties, operators, ui, utils

import bpy

# 2. List all classes to be registered
# Typically, you'd collect these from the other files
classes = (
    properties.TextureCycleProperties,
    operators.OT_CycleTextures,
    operators.OT_RestoreTextures,
    ui.VIEW3D_PT_TextureCycle,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    # Create a global pointer to our properties on the Scene
    bpy.types.Scene.texture_cycle_data = bpy.props.PointerProperty(
        type=properties.TextureCycleProperties
    )

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    del bpy.types.Scene.texture_cycle_data

if __name__ == "__main__":
    register()
