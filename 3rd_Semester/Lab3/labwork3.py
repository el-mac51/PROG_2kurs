def gen_bin_tree(height=4, root=4, left_leaf=lambda x: x * 4, right_leaf=lambda x: x + 1):
    """
    генерирует бинарное дерево 
    
    эта функция рекурсивно создает бинарное дерево, где каждый узел представлен
    в виде кортежа (value, left_child, right_child). Дерево строится с использованием
    предоставленных функций для генерации дочерних узлов.
    
    Args:
        height (int): максимальная высота дерева 
        root: значение корневого узла
        left_leaf (callable): функция для генерации значения левого потомка из значения родителя
        right_leaf (callable): Функция для генерации значения правого потомка из значения родителя
    
    Returns:
        tuple or None: Корневой узел сгенерированного бинарного дерева в формате 
                      (value, left, right), или None если высота равна 0.
    """
    def build_tree(current_root, current_height=1):
        if current_height > height:
            return None
        
        if current_height == height:
            return (current_root, None, None)
        
        left_child = build_tree(left_leaf(current_root), current_height + 1)
        right_child = build_tree(right_leaf(current_root), current_height + 1)
        
        return (current_root, left_child, right_child)
    
    if height <= 0:
        return None
    
    return build_tree(root)
