import unittest
from labwork3 import gen_bin_tree

class TestTree(unittest.TestCase):

    def test_creation(self):
        """прверяем что дерево создается"""
        root = gen_bin_tree(height=1, root=4)
        self.assertIsNotNone(root)
        self.assertEqual(root[0], 4)
        self.assertIsNone(root[1])
        self.assertIsNone(root[2])

    def test_height_2(self):
        """проверяем два уровня дерева"""
        root = gen_bin_tree(height=2, root=4)
        self.assertEqual(root[0], 4)
        
        self.assertIsNotNone(root[1])
        self.assertEqual(root[1][0], 16)
        self.assertIsNotNone(root[2])
        self.assertEqual(root[2][0], 5)

        self.assertIsNone(root[1][1])
        self.assertIsNone(root[1][2])
        self.assertIsNone(root[2][1])
        self.assertIsNone(root[2][2])

    def test_edges(self):
        """проверяем крайние значения с нулевым и отрицательным значениями"""
        self.assertIsNone(gen_bin_tree(height=0, root=4))
        self.assertIsNone(gen_bin_tree(height=-1, root=4))

    def test_formula(self):
        """проверяем формулы для узлов с обоих сторон"""
        root = gen_bin_tree(height=2, root=10)        
        self.assertEqual(root[1][0], 40)
        self.assertEqual(root[2][0], 11)

    def test_node_count(self):
        """проверяем количество узлов в дереве"""
        def count_nodes(node):
            if node is None:
                return 0
            return 1 + count_nodes(node[1]) + count_nodes(node[2])
    
        root = gen_bin_tree(height=4, root=4)
        nodes = count_nodes(root)
        self.assertEqual(nodes, 15)

if __name__ == "__main__":
    unittest.main()
