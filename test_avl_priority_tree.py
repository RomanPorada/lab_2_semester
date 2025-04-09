import unittest
from avl_priority_queue import (
    Node,
    insert,
    delete_node,
    get_balance,
    get_min_value_node,
    extract_max_priority,
)

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.root = None
        self.root = insert(self.root, "A", 10)
        self.root = insert(self.root, "B", 20)
        self.root = insert(self.root, "C", 5)
        self.root = insert(self.root, "D", 6)
        self.root = insert(self.root, "E", 15)

    def test_insert_structure(self):
        def find_by_priority(node, priority):
            if not node:
                return None
            if node.priority == priority:
                return node
            elif priority < node.priority:
                return find_by_priority(node.left, priority)
            else:
                return find_by_priority(node.right, priority)

        priorities = [10, 20, 5, 6, 15]
        for p in priorities:
            node = find_by_priority(self.root, p)
            self.assertIsNotNone(node, f"Node with priority {p} not found in the tree")


    def test_balance_after_insert(self):
        balance = get_balance(self.root)
        self.assertTrue(-1 <= balance <= 1, "Tree is unbalanced after insert")

    def test_get_min_value_node(self):
        min_node = get_min_value_node(self.root)
        self.assertEqual(min_node.priority, 5)
        self.assertEqual(min_node.value, "C")

    def test_delete_node(self):
        self.root = delete_node(self.root, 5)
        min_node = get_min_value_node(self.root)
        self.assertNotEqual(min_node.priority, 5)

    def test_extract_max_priority(self):
        self.root = extract_max_priority(self.root)
        min_node = get_min_value_node(self.root)
        self.assertNotEqual(min_node.priority, 5)

    def test_multiple_operations_balance(self):
        self.root = delete_node(self.root, 10)
        self.root = insert(self.root, "F", 3)
        self.root = insert(self.root, "G", 7)
        balance = get_balance(self.root)
        self.assertTrue(-1 <= balance <= 1, "Tree is unbalanced after multiple operations")

if __name__ == "__main__":
    unittest.main()
