import unittest
from lab_5 import mark_unsafe_cells, build_graph, bfs

class TestSafePathFinder(unittest.TestCase):

    def setUp(self):
        self.matrix_all_safe = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]

        self.matrix_with_sensor = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]

    def test_mark_unsafe_cells(self):
        unsafe = mark_unsafe_cells(self.matrix_with_sensor)
        self.assertTrue(all(all(row) for row in unsafe))

        unsafe = mark_unsafe_cells(self.matrix_all_safe)
        self.assertFalse(any(any(row) for row in unsafe))

    def test_build_graph_all_safe(self):
        unsafe = mark_unsafe_cells(self.matrix_all_safe)
        graph = build_graph(self.matrix_all_safe, unsafe)
        self.assertEqual(len(graph), 9)

    def test_bfs_path_exists(self):
        matrix = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        unsafe = mark_unsafe_cells(matrix)
        graph = build_graph(matrix, unsafe)
        path_length = bfs(graph, matrix)

        self.assertEqual(path_length, 2)



    def test_bfs_no_path(self):
        matrix = [
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1]
        ]
        unsafe = mark_unsafe_cells(matrix)
        graph = build_graph(matrix, unsafe)
        path_length = bfs(graph, matrix)
        self.assertEqual(path_length, -1)

if __name__ == '__main__':
    unittest.main()
