import unittest
from random import randint

text = input("Введіть тест для тусту, щось інше для запуску: ")

def range_search(lst):
    start_index = 0
    finish_index = 0
    
    list_sort = sorted(lst)
    
    if lst == list_sort:
        return (-1, -1)

    for el in range(len(lst)):
        if lst[el] != list_sort[el]:
            start_index = el
            break

    for el in range(len(lst) - 1, -1, -1):
        if lst[el] != list_sort[el]:
            finish_index = el
            break
    
    return (start_index, finish_index)

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
if text == "тест":
    if __name__ == "__main__":
        unittest.main()
else:
    list = [randint(1, 19) for _ in range(9)]
    print(list)

    index = range_search(list)
    print(index)