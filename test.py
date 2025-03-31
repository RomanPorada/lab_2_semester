import unittest
from lab_3 import balanced_tree

class TestRangeSearch(unittest.TestCase):
    def test_balanced_tree_true(self):
        self.assertEqual(balanced_tree("tree_2.txt"), True)
    
    def test_balanced_tree_false(self):
        self.assertEqual(balanced_tree("tree.txt"), False)
    
unittest.main()