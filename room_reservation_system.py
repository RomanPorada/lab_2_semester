from avl_priority_queue import height, right_rotate, left_rotate, get_balance

class Node():
    def __init__(self, numer, name: str):
        self.numer = numer
        self.name = name
        self.left = None
        self.right = None
        self.height = 1

def insert(node, numer, name):
    if node is None:
        return Node(numer, name)
    
    if numer < node.numer:
        node.left = insert(node.left, numer, name)
    elif numer > node.numer:
        node.right = insert(node.right, numer, name)
    else:
        print("Даний номер вже зарезервований, виберіть інший номер")

    node.height = 1 + max(height(node.left), height(node.right))

    balance = get_balance(node) 

    if balance > 1 and numer < node.left.numer:
        return right_rotate(node)
    if balance < -1 and numer > node.right.numer:
        return left_rotate(node)
    if balance > 1 and numer > node.left.numer:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if balance < -1 and numer < node.right.numer:
        node.right = right_rotate(node.right)
        return left_rotate(node)
    
    return node

def get_min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node, numer):
    if node is None:
        print("Цей номер не заброньовано")
        return node
    
    numer = int(numer)
    if numer < node.numer:
        node.left = delete(node.left, numer)
    elif numer > node.numer:
        node.right = delete(node.right, numer)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.right
            node = None
            return temp
        temp = get_min_value_node(node.right)
        node.numer = temp.numer
        node.name = temp.name
        node.right = delete(node.right, temp.numer)

    node.height = 1 + max(height(node.left), height(node.right))
    balance = get_balance(node)

    if balance > 1 and get_balance(node.left) >= 0:
        return right_rotate(node)
    if balance > 1 and get_balance(node.left) < 0:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if balance < -1 and get_balance(node.right) <= 0:
        return left_rotate(node)
    if balance < -1 and get_balance(node.right) > 0:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node
    

def search(node, numer):
    if node is None:
        print("Цей номер не є заброньованим")
        return None
    elif node.numer == numer:
        print(F"Номер {numer} заброньовано")
        return node
    elif numer < node.numer:
        return search(node.left, numer)
    elif numer > node.numer:
        return search(node.right, numer)

def list_reservation_room(node):
    if node == None:
        return
    
    list_reservation_room(node.left)
    print(f"Номер {node.numer} заброньована {node.name}")
    list_reservation_room(node.right)

def draw_tree_in_console(node, prefix = "", is_left = True):
    if  node is not None:
        draw_tree_in_console(node.right, prefix + ("|   " if is_left else "   "), False)
        print(prefix + ("└── " if is_left else "┌── ") + f"[{node.numer}] {node.name}")
        draw_tree_in_console(node.left, prefix + ("    " if is_left else "│   "), True)

root = None
while True:
    action = input("Введіть дію яку хочете виконати: ")

    if action == "break":
        break
    elif action == "add":
        add = input("Введіть номер для броні та імя бронювальника(дані вводити через кому): ").split(",")
        root = insert(root, int(add[0]), add[1])
    elif action == "delete":
        while True:
            try:
                deleted = int(input("Введіть номер кімнати, з якої хочете зняти бронь: "))
                break
            except ValueError:
                print("Введіть число")
        root = delete(root, deleted)
    elif action == "reservation":
        list_reservation_room(root)
    elif action == "draw":
        draw_tree_in_console(root)
    elif action == "check":
        while True:
            try:
                check = int(input("Введіть номер кімнати, яку хочете перевірити на заброньованість: "))
                break
            except ValueError:
                print("Введіть число")
        search(root, check)
