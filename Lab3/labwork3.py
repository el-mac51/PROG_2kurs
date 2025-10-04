class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree(root, max_height, current_height = 1):
    if current_height > max_height:
        return None
    node = TreeNode(root)
    if current_height < max_height:
        node.left = tree(root * 4, max_height, current_height + 1)
        node.right = tree(root + 1, max_height, current_height + 1)
    return node

my_tree = tree(root = 4, max_height = 4)

# def print_tree(root, level=0, prefix=""): #код для вывода дерева
#     if root is not None:
#         print_tree(root.right, level + 1, "/--- ")
#         if level == 0:
#             print(" " * (level * 6) + "Root: " + str(root.value))
#         else:
#             print(" " * (level * 6) + prefix + str(root.value))
#         print_tree(root.left, level + 1, "\\--- ")
# my_tree = tree(root=4, max_height=4)
# print_tree(my_tree)