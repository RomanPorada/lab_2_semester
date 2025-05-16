import unittest

from lab_7 import search 

class TestKMPSearch(unittest.TestCase):
    def test_basic_match(self):
        self.assertEqual(search("abcabcabc", "abc"), [0, 3, 6])

    def test_single_match(self):
        self.assertEqual(search("hello world", "world"), [6])

    def test_no_match(self):
        self.assertEqual(search("abcdef", "gh"), [])

    def test_empty_needle(self):
        self.assertEqual(search("abcdef", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(search("", "a"), [])

    def test_both_empty(self):
        self.assertEqual(search("", ""), [])

    def test_partial_overlap(self):
        self.assertEqual(search("aaaabaaaab", "aaab"), [1, 6])

    def test_case_sensitive(self):
        self.assertEqual(search("aAaAaA", "AaA"), [1, 3])

    def test_full_match(self):
        self.assertEqual(search("pattern", "pattern"), [0])

    def test_overlap_matches(self):
        self.assertEqual(search("aaaaa", "aaa"), [0, 1, 2])

if __name__ == "__main__":
    unittest.main()
