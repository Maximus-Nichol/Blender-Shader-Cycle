import bpy
import pytest

@pytest.fixture
def setup_test_material():

    # Create a clean mesh and material
    bpy.ops.mesh.primitive_cube_add()
    obj = bpy.context.active_object

    mat = bpy.data.materials.new(name="Test_Material")
    mat.use_nodes = True
    obj.data.materials.append(mat)

    # Standard Principled BSDF setup check
    nodes = mat.node_tree.nodes
    nodes.clear()
    output = nodes.new(type="ShaderNodeOutputMaterial")
    principled = nodes.new(type="ShaderNodeBsdfPrincipled")
    mat.node_tree.links.new(principled.outputs[0], output.inputs["Surface"])

    yield mat, principled

    # Cleanup after test
    bpy.data.materials.remove(mat)
    bpy.data.objects.remove(obj, do_unlink=True)