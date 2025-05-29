import unittest
import tempfile
import os
from lab_8 import kruskal_mst

class TestKruskalMST(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', newline='')
        self.temp_file.write(
            "A,B,1\n"
            "B,C,2\n"
            "C,D,3\n"
            "D,A,4\n"
            "A,C,5\n"
        )
        self.temp_file.close()
        self.filename = self.temp_file.name

    def tearDown(self):
        os.remove(self.filename)

    def test_kruskal_mst_valid(self):
        weight, mst_edges, _ = kruskal_mst(self.filename)
        self.assertEqual(weight, 6)
        self.assertEqual(len(mst_edges), 5)

    def test_disconnected_graph(self):
        with open(self.filename, 'w') as f:
            f.write("A,B,1\n")
            f.write("C,D,2\n")
        result = kruskal_mst(self.filename)
        self.assertEqual(result, (-1, [(1, 'A', 'B'), (2, 'C', 'D')], []))

    def test_single_node(self):
        with open(self.filename, 'w') as f:
            f.write("A,A,0\n")
        result = kruskal_mst(self.filename)
        self.assertEqual(result, (0, [(0, 'A', 'A')], []))

    def test_empty_file(self):
        with open(self.filename, 'w') as f:
            pass
        result = kruskal_mst(self.filename)
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()
