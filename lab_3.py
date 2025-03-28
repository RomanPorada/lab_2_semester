class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    if not lines:
        return None

    values = []
    for line in lines:
        values.extend(line.split())

    root = BinaryTree(int(values[0])) if values[0] != "None" else None
    if not root:
        return None

    queue = [root]
    index = 1

    while queue and index < len(values):
        current = queue.pop(0)

        if current:
            left_value = values[index] if index < len(values) else "None"
            right_value = values[index + 1] if index + 1 < len(values) else "None"

            current.left = BinaryTree(int(left_value)) if left_value != "None" else None
            current.right = BinaryTree(int(right_value)) if right_value != "None" else None

            queue.append(current.left)
            queue.append(current.right)

            index += 2

    return root

def is_tree_balanced(node: BinaryTree) -> bool:
    if not node:
        return True

    stack = [(node, 0)]
    heights = {}

    while stack:
        current, state = stack.pop()

        if current is None:
            heights[None] = 0
            continue

        if state == 0:
            stack.append((current, 1))
            stack.append((current.left, 0))
            stack.append((current.right, 0))
        else:
            left_height = heights[current.left]
            right_height = heights[current.right]

            if abs(left_height - right_height) > 1:
                return False

            heights[current] = 1 + max(left_height, right_height)

    return True

file_path = "tree.txt"
root = build_tree_from_file(file_path)

print(is_tree_balanced(root))
