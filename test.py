import unittest
import tempfile
import os

from lab_6 import solve_beer_problem, read_input

class TestBeerProblem(unittest.TestCase):
    def create_temp_input_file(self, n, b, preferences):
        tmp = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        tmp.write(f"{n} {b}\n")
        tmp.write(' '.join(preferences) + "\n")
        tmp.close()
        return tmp.name

    def test_case_1(self):
        file_path = self.create_temp_input_file(2, 2, ["YN", "NY"])
        n, b, prefs = read_input(file_path)
        self.assertEqual(n, 2)
        self.assertEqual(b, 2)
        os.replace(file_path, "src/input.txt")
        self.assertEqual(solve_beer_problem(), 2)
        os.remove("src/input.txt")

    def test_case_2(self):
        file_path = self.create_temp_input_file(6, 3, ["YNN", "YNY", "YNY", "NYY", "NYY", "NYN"])
        n, b, prefs = read_input(file_path)
        self.assertEqual(n, 6)
        self.assertEqual(b, 3)
        os.replace(file_path, "src/input.txt")
        self.assertEqual(solve_beer_problem(), 2)
        os.remove("src/input.txt")

    def test_all_like_same_beer(self):
        file_path = self.create_temp_input_file(3, 3, ["YNN", "YNN", "YNN"])
        os.replace(file_path, "src/input.txt")
        self.assertEqual(solve_beer_problem(), 1)
        os.remove("src/input.txt")

if __name__ == '__main__':
    unittest.main()
