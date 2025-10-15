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

def print_tree(root, level=0, prefix=""): #код для вывода дерева
    if root is not None:
        print_tree(root.right, level + 1, "/--- ")
        if level == 0:
            print(" " * (level * 6) + "Root: " + str(root.value))
        else:
            print(" " * (level * 6) + prefix + str(root.value))
        print_tree(root.left, level + 1, "\\--- ")
my_tree = Ttree(root_value = 4, max_height = 4)
print_tree(my_tree)
