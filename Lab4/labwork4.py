class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        """Инициализирует узел бинарного дерева
        Args:
            value: целочисленное значение для хранения в узле"""

def Ttree(root_value, max_height,
          left_formula = lambda x: x * 4,
          right_formula = lambda x: x + 1):
    
    """ Создает бинарное дерево с параметризуемыми формулами

        Дерево строится итеративно с использооанием очереди (обход в ширину)
        каждый узел с глубиной меньше max_height получает двух потомков, значения которых
        вычисляются по формулам от значения родительского узла.

    Args:
        root_value: значение корневого узла
        max_height: максимальная высота дерева
        left_formula: функция для вычисления левого потомка 
        right_formula: функция для вычисления правого потомка"""
    
    if max_height <= 0:
        return None
     
    root = Treenode(root_value)
    queue = [] # создание пустой очереди
    queue.append((root, 1))

    while queue:
        current_node, current_depth = queue.pop(0)
        if current_depth < max_height:
                left_value = left_formula(current_node.value)
                left_child = Treenode(left_value)
                current_node.left = left_child
                queue.append((left_child, current_depth + 1))

                right_value = right_formula(current_node.value)
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
