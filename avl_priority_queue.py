from random import randint

class Node():
    def __init__(self, value, priority=None):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    return node.height if node else 0

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y

def get_balance(node):
    return height(node.left) - height(node.right) if node else 0

def insert(node, value, priority):
    if not node:
        return Node(value, priority)
    
    if priority < node.priority:
        node.left = insert(node.left, value, priority)
    else:
        node.right = insert(node.right, value, priority)
    
    node.height = 1 + max(height(node.left), height(node.right))

    balance = get_balance(node)

    if balance > 1 and priority < node.left.priority:
        return right_rotate(node)
    
    if balance < -1 and priority >= node.right.priority:
        return left_rotate(node)
    
    if balance > 1 and priority >= node.left.priority:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    
    if balance < -1 and priority < node.right.priority:
        node.right = right_rotate(node.right)
        return left_rotate(node)
    
    return node

def get_min_value_node(node):
    """Знаходить вузол з найменшим значенням пріоритету (найлівіший)"""
    if node.left is None:
        return node
    return get_min_value_node(node.left)

def delete_node(root, priority):
    """Видаляє вузол за пріоритетом та перебалансовує дерево"""
    if root is None:
        return root

    if priority < root.priority:
        root.left = delete_node(root.left, priority)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = get_min_value_node(root.right)
        root.value, root.priority = temp.value, temp.priority
        root.right = delete_node(root.right, temp.priority)

    if root is None:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)

    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)

    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)

    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def extract_max_priority(root):
    """Видаляє елемент із найбільшим пріоритетом (найменший priority)"""
    min_node = get_min_value_node(root)
    if min_node:
        print(f"Extracting: ({min_node.value}, p={min_node.priority})")
        root = delete_node(root, min_node.priority)
    return root
if __name__ == "__main__":
    root = None
    for _ in range(7):
        val = randint(1, 19)
        prio = randint(1, 19)
        print(f"Inserting: {val} with priority {prio}")
        root = insert(root, val, prio)

    print("\n\nExtracting elements in order of priority:")
    while root is not None:
        root = extract_max_priority(root)

    print("\nAll elements extracted, queue is empty!")
