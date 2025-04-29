import time

class Node():
    def __init__(self, employee_id, number_like_beer, list_beer_like = []):
        self.employee_id = employee_id
        self.list_like_beer = list_beer_like
        self.number_like_beer = number_like_beer
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

def insert(node, id, number_like_beer, lst):
    if not node:
        return Node(id, number_like_beer, lst)
    
    if number_like_beer < node.number_like_beer:
        node.left = insert(node.left, id, number_like_beer, lst)
    else:
        node.right = insert(node.right, id, number_like_beer, lst)

    node.height = 1 + max(height(node.left), height(node.right))

    balance = get_balance(node)

    if balance > 1 and number_like_beer < node.left.number_like_beer:
        return right_rotate(node)
    if balance < -1 and number_like_beer >= node.right.number_like_beer:
        return left_rotate(node)
    if balance > 1 and number_like_beer >= node.left.number_like_beer:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if balance < -1 and number_like_beer < node.right.number_like_beer:
        node.right = right_rotate(node.right)
        return left_rotate(node)
    
    return node

def get_most_picky_employee(node):
    current = node
    while current.left:
        current = current.left
    return current

def remove_satisfied(node, selected_beer):
    if not node:
        return None
    
    node.left = remove_satisfied(node.left, selected_beer)
    node.right = remove_satisfied(node.right, selected_beer)

    if any(beer in selected_beer for beer in node.list_like_beer): 
        return merge_trees(node.left, node.right)
    node.height = 1 + max(height(node.left), height(node.right))
    return node

def merge_trees(left, right):
    if not left:
        return right
    if not right:
        return left
    
    most_left = right
    while most_left.left:
        most_left = most_left.left
    most_left.left = left
    return right

def read_input(filename):
    with open(filename, "r") as f:
        n, b = map(int, f.readline().split())
        data = f.read().replace("\n", "").split()
    matrix = []
    for row in data:
        matrix.append([i for i, c in enumerate(row) if c == "Y"])
    return n, b, matrix

def solve_beer_problem():
    start = time.perf_counter()
    n, b, preferences = read_input("input.txt")
    root = None
    for i in range(n):
        root = insert(root, i, len(preferences[i]), preferences[i])

    selected_beers = set()

    while root:
        picky = get_most_picky_employee(root)
        if len(picky.list_like_beer) == 1:
            beer = picky.list_like_beer[0]
        else:
            count = [0] * b
            def count_beers(node):
                if not node: return
                for beer in node.list_like_beer:
                    count[beer] += 1     
                count_beers(node.left)
                count_beers(node.right)
            count_beers(root)
            beer = max(picky.list_like_beer, key= lambda x: count[x])
        selected_beers.add(beer)
        root = remove_satisfied(root, selected_beers)
    finish = time.perf_counter()
    print(finish - start)

    return len(selected_beers)


if __name__ == "__main__":
    print(solve_beer_problem())
