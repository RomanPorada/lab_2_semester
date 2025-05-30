import unittest
from math import sqrt

from lab_9 import search_max_len_cable



class TestCableLength(unittest.TestCase):
    def test_search_max_len_cable(self):
        w = 2
        heights = [1, 3, 2]
        result = search_max_len_cable(w, heights)
        expected = 5.66
        self.assertAlmostEqual(result, expected, places=2)

    def test_flat_heights(self):
        w = 1
        heights = [2, 2, 2]
        expected = round(2 * sqrt(2), 2)
        result = search_max_len_cable(w, heights)
        self.assertAlmostEqual(result, expected, places=2)

unittest.main()
