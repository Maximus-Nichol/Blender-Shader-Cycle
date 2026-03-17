import bpy

def get_node_colour(node):
    # 1. Check for Principled BSDF
    if "Base Colour" in node.inputs:
        return node.inputs["Base Colour"].default_value[:]
    
    # 2. Check for 'Color' (Diffuse BSDF, Emission, etc.)
    if "Colour" in node.inputs:
        return node.inputs["Colour"].default_value[:]
        
    # 3. Fallback to viewport color
    return (0.8, 0.8, 0.8, 1.0)

def find_output_node(material):
    # Finds material output
    if not material.node_tree:
        return None
    for node in material.node_tree.nodes:
        if node.type == 'OUTPUT_MATERIAL' and node.is_active_output:
            return node
    return None
