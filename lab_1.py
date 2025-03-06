import unittest
from random import randint

def range_search(lst):
    if len(lst) < 2:
        return (-1, -1)
    
    start_index, finish_index = 0, 0
    element = lst[0]
    precipice = False
    
    for i in range(len(lst)):
        if not precipice:
            if lst[i] >= element:
                element = lst[i]
            else:
                precipice = True
                smolest_element = lst[i]
        else:
            if lst[i] < smolest_element:
                smolest_element = lst[i]
    
    if not precipice:
        return (-1, -1)
    
    for i in range(len(lst)):
        if lst[i] > smolest_element:
            start_index = i
            break
    
    element = lst[-1]
    precipice = False
    
    for i in range(len(lst) - 1, -1, -1):
        if not precipice:
            if lst[i] <= element:
                element = lst[i]
            else:
                precipice = True
                biggest_element = lst[i]
        else:
            if lst[i] > biggest_element:
                biggest_element = lst[i]
    
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] < biggest_element:
            finish_index = i
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


lst = [randint(1, 19) for _ in range(9)]
print(lst)
index = range_search(lst)
print(index)
