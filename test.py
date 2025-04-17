import unittest
from collections import deque
from lab_5 import mark_unsafe_cells, is_safe, bfs

class TestPathfinding(unittest.TestCase):

    def test_mark_unsafe_cells(self):
        matrix = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        unsafe = mark_unsafe_cells(matrix)
        expected = [
            [True, True, True],
            [True, True, True],
            [True, True, True]
        ]
        self.assertEqual(unsafe, expected)

    def test_is_safe(self):
        matrix = [
            [1, 1],
            [1, 1]
        ]
        unsafe = [
            [False, True],
            [False, False]
        ]
        visited = [
            [False, False],
            [True, False]
        ]
        self.assertTrue(is_safe(0, 0, matrix, unsafe, visited))
        self.assertFalse(is_safe(0, 1, matrix, unsafe, visited))
        self.assertFalse(is_safe(1, 0, matrix, unsafe, visited))
        self.assertTrue(is_safe(1, 1, matrix, unsafe, visited))

    def test_bfs_with_path(self):
        matrix = [
            [1, 1, 1],
            [0, 1, 0],
            [1, 1, 1]
        ]
        unsafe = mark_unsafe_cells(matrix)
        result = bfs(matrix, unsafe)
        self.assertEqual(result, -1)  

    def test_bfs_without_obstacles(self):
        matrix = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        unsafe = mark_unsafe_cells(matrix)
        result = bfs(matrix, unsafe)
        self.assertGreaterEqual(result, 2)  

    def test_bfs_no_path(self):
        matrix = [
            [0, 1, 1],
            [0, 1, 1],
            [0, 1, 1]
        ]
        unsafe = mark_unsafe_cells(matrix)
        result = bfs(matrix, unsafe)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
