import unittest
from avl_priority_queue import height, right_rotate, left_rotate, get_balance
from room_reservation_system import Node, insert, delete, search, get_min_value_node

class TestRoomReservationTree(unittest.TestCase):
    def setUp(self):
        self.root = None
        self.root = insert(self.root, 101, "Ivan")
        self.root = insert(self.root, 203, "Oksana")
        self.root = insert(self.root, 99, "Andriy")
        self.root = insert(self.root, 150, "Olha")

    def test_insert_and_structure(self):
        def find(node, numer):
            if node is None:
                return None
            if numer == node.numer:
                return node
            elif numer < node.numer:
                return find(node.left, numer)
            else:
                return find(node.right, numer)

        self.assertIsNotNone(find(self.root, 101))
        self.assertIsNotNone(find(self.root, 203))
        self.assertIsNotNone(find(self.root, 99))
        self.assertEqual(find(self.root, 150).name, "Olha")

    def test_delete_node(self):
        self.root = delete(self.root, 203)
        node = search(self.root, 203)
        self.assertIsNone(node)

    def test_get_min_value_node(self):
        min_node = get_min_value_node(self.root)
        self.assertEqual(min_node.numer, 99)
        self.assertEqual(min_node.name, "Andriy")

    def test_search_existing(self):
        result = search(self.root, 101)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Ivan")

    def test_search_nonexistent(self):
        result = search(self.root, 777)
        self.assertIsNone(result)

    def test_balance_after_operations(self):
        self.root = delete(self.root, 99)
        self.root = insert(self.root, 300, "Yurii")
        balance = get_balance(self.root)
        self.assertTrue(-1 <= balance <= 1, "Tree is unbalanced")

if __name__ == "__main__":
    unittest.main()
