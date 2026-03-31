import bpy

class MaterialBackup(bpy.types.PropertyGroup):
    """
    Stores the state of a material 
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
    is_cycled: bpy.props.BoolProperty(default=False)
    
    shader_type: bpy.props.EnumProperty(
        name="Shader Type",
        description="Choose between presets shader (TODO: or custom)",
        items=[
            ('EMISSION', "Emission", "Cycles to a flat Emission shader"),
            ('TOON', "Toon", "Cycles to a Diffuse Toon shader")
        ],
        default='EMISSION'
    )
    
    backup_data: bpy.props.CollectionProperty(
        type=MaterialBackup,
        description="A collection of all materials and their original node connections"
    )
