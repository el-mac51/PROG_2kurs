import unittest

class TreeNode: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree(root, max_height, current_height = 1): #основной код дерева
    if current_height > max_height:
        return None
    node = TreeNode(root)
    if current_height < max_height:
        node.left = tree(root * 4, max_height, current_height + 1)
        node.right = tree(root + 1, max_height, current_height + 1)
    return node

my_tree = tree(root = 4, max_height = 4)

class TestTree(unittest.TestCase):

    def test_creation(self):

        root = tree(4,1)
        self.assertIsNotNone(root)
        self.assertEqual(root.value, 4)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_height_2(self): #проверям дерево высотой 2

        root = tree(4, 2) #это высота 1
        self.assertEqual(root.value, 4) #проверяем корень дерева
        
        self.assertIsNotNone(root.left) #это высота 2
        self.assertEqual(root.left.value, 16)
        self.assertIsNotNone(root.right)
        self.assertEqual(root.right.value, 5)

        self.assertIsNone(root.left.left) #проевряем что после 2й высоты ничего
        self.assertIsNone(root.left.right)
        self.assertIsNone(root.right.left)
        self.assertIsNone(root.right.right)

    def test_edges(self): #проверяем что на нулевой и отрицательной высотах ничего
        self.assertIsNone(tree(4, 0))
        self.assertIsNone(tree(4, -1))

    def test_formula(self):
        root = tree(10, 2)        
        self.assertEqual(root.left.value, 40)  #проверяем формулы для левых и правых узлов
        self.assertEqual(root.right.value, 11) 

    def test_node_count(self):

        def count_nodes(node): #считаем узлы

            if node is None: # если узлов нет
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)
    
        root = tree(4, 4) #проверяем для наших значений дерева
        nodes = count_nodes(root)
        self.assertEqual(nodes, 15) #в дереве высотой 4 должно быть 15 узлов
        
if __name__ == "__main__":
    unittest.main()