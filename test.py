import unittest
from lab_1 import range_search

class TestRangeSearch(unittest.TestCase):
    def test_unsorted_middle(self):
        self.assertEqual(range_search([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), (3, 9))
    
    def test_sorted_array(self):
        self.assertEqual(range_search([1, 2, 3, 4, 5, 6, 7, 8, 9]), (-1, -1))
    
    def test_reverse_sorted_array(self):
        self.assertEqual(range_search([9, 8, 7, 6, 5, 4, 3, 2, 1]), (0, 8))
    
    def test_single_element(self):
        self.assertEqual(range_search([1]), (-1, -1))
    
    def test_all_equal_elements(self):
        self.assertEqual(range_search([5, 5, 5, 5, 5]), (-1, -1))
    
    def test_unsorted_start_and_end(self):
        self.assertEqual(range_search([10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 20]), (0, 9))


unittest.main()