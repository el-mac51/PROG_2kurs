import unittest

class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def Ttree(root_value, max_height):
    if max_height <= 0:
        return None
    root = Treenode(root_value)
    queue = [] # создание пустой очереди
    queue.append((root, 1))

    while queue:
        current_node, current_depth = queue.pop(0)
        if current_depth < max_height:
                left_value = current_node.value * 4
                left_child = Treenode(left_value)
                current_node.left = left_child
                queue.append((left_child, current_depth + 1))

                right_value = current_node.value + 1
                right_child = Treenode(right_value)
                current_node.right = right_child
                queue.append((right_child, current_depth + 1))
    return root

my_tree = Ttree(root_value = 4, max_height = 4)

class TestTree(unittest.TestCase):

    def test_creation(self):

        root = Ttree(4,1)

        self.assertIsNotNone(root)
        self.assertEqual(root.value, 4)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_height_2(self): #проверям дерево высотой 2

        root = Ttree(4, 2) #это высота 1
        self.assertEqual(root.value, 4) #проверяем корень дерева
        
        self.assertIsNotNone(root.left) #это высота 2
        self.assertEqual(root.left.value, 16)
        self.assertIsNotNone(root.right)
        self.assertEqual(root.right.value, 5)

        self.assertIsNone(root.left.left) #проевряем что после 2й высоты ничего
        self.assertIsNone(root.left.right)
        self.assertIsNone(root.right.left)
        self.assertIsNone(root.right.right)

    def test_edges(self):

        self.assertIsNone(Ttree(4, 0))
        self.assertIsNotNone(Ttree(4, 1))
        self.assertIsNotNone(Ttree(4, 2))
        self.assertIsNotNone(Ttree(4, 3)) 
        self.assertIsNotNone(Ttree(4, 4))   

    def test_node_creation(self):

        node = Treenode(5)
        self.assertEqual(node.value, 5)          # проверка значения
        self.assertIsNone(node.left)             # проверка что left = None
        self.assertIsNone(node.right)            # проверка что right = None

    def test_left_child_formula(self):

        tree = Ttree(4, 2)
        self.assertEqual(tree.left.value, 16)    # 4 * 4 = 16
        self.assertEqual(tree.left.value, tree.value * 4)

    def test_tree_formulas(self):

        root = Ttree(10, 2)
        self.assertEqual(root.left.value, 40)  
        self.assertEqual(root.right.value, 11) 

if __name__ == "__main__":
    unittest.main()
