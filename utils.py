import bpy

def get_node_color(node):
    # Specifically handles the most common shader
    if node.type == 'BSDF_PRINCIPLED':
        return node.inputs["Base Color"].default_value[:]
    
    # Search for any input with "Color" in the name
    # Covers Emission, Diffuse, Mix, etc.
    for input in node.inputs:
        if "Color" in input.name:
            return input.default_value[:]
            
    return (0.8, 0.8, 0.8, 1.0)

def find_output_node(material):
    # Finds material output
    if not material.node_tree:
        return None
    for node in material.node_tree.nodes:
        if node.type == 'OUTPUT_MATERIAL' and node.is_active_output:
            return node
    return None
