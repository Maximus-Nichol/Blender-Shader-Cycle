import bpy

class MaterialBackup(bpy.types.PropertyGroup):
    """
    A simple data structure to store the state of a material 
    before it was cycled.
    """
    material_name: bpy.props.StringProperty(
        name="Material Name",
        description="The name of the material being backed up"
    )
    
    original_node_name: bpy.props.StringProperty(
        name="Original Node Name",
        description="The name of the node previously connected to the Material Output"
    )

class TextureCycleProperties(bpy.types.PropertyGroup):
    """
    Global settings and state for the Texture Cycle add-on.
    Attached to bpy.types.Scene.
    """
    is_cycled: bpy.props.BoolProperty(
        name="Is Cycled",
        description="Tracks if the scene is currently in diagnostic mode",
        default=False
    )
    
    backup_data: bpy.props.CollectionProperty(
        type=MaterialBackup,
        description="A collection of all materials and their original node connections"
    )
