import unittest
import bpy

class TestTextureCycle(unittest.TestCase):
    def test_node_creation(self):

        test_mat = bpy.data.materials.new(name="TestMaterial")
        test_mat.use_nodes = True
        
        bpy.ops.texture_cycle.cycle_mats()
        
        node_names = [node.name for node in test_mat.node_tree.nodes]
        self.assertIn("TC_CYCLED_SHADER", node_names)

        bpy.data.materials.remove(test_mat)

if __name__ == '__main__':
    unittest.main()
