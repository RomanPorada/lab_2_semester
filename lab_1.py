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
    else:
        
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

lst = [randint(1, 19) for _ in range(9)]
print(lst)
index = range_search(lst)
print(index)
