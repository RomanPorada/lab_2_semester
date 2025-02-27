from random import randint

def range_search(list):
    start_index = 0
    finish_index = 0
    
    list_sort = list[:]
    ln = len(list_sort)
    for el in range(ln):
        replacement = 0
        for j in range(0, ln-el-1):
            if list_sort[j] > list_sort[j + 1]:
                list_sort[j], list_sort[j + 1] = list_sort[j + 1], list_sort[j]
                replacement += 1
        if replacement == 0:
            break
        
        

        
    if list == list_sort:
        return (-1, -1)

    for el in range(len(list)):
        if list[el] != list_sort[el]:
            start_index = el
            break

    for el in range(len(list) -1, -1, -1):
        if list[el] != list_sort[el]:
            finish_index  = el
            break
    
    return (start_index, finish_index)
    

list = [randint(1, 19) for _ in range(9)]
print(list)

index = range_search(list)
print(index)
              