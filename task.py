from random import randint

def more_range_search(lst):
    if len(lst) < 2:
        return (-1, -1)
    
    start_index, finish_index = 0, 0
    element = lst[0]
    precipice = False
    indexs = []
    
    for i in range(len(lst)):
        if not precipice:
            if lst[i] >= element:
                element = lst[i]
            else:
                precipice = True
                smolest_element = lst[i]
                biggest_element = element
        else:
            if lst[i] < smolest_element:
                smolest_element = lst[i]
            elif lst[i] > biggest_element:
                finish_index = i - 1
                for j in range(len(lst)):
                    if lst[j] >= biggest_element:
                        start_index = j
                        indexs.append((start_index, finish_index))
                        precipice = False
                        break
    
    return indexs
    
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 6, 5, 7, 9, 8]
    print(lst)
    index = more_range_search(lst)
    print(index)
