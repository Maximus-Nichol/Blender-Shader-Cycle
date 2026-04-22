import bpy
import pytest

def test_node_creation(setup_test_material):

    mat, principled = setup_test_material
    bpy.ops.texture_cycle.cycle_mats()
    node_names = [node.name for node in mat.node_tree.nodes]
    
    assert "TC_CYCLED_SHADER" in node_names, "The cycle node was not found in the material node tree."
