from random import randint

def more_range_search(lst):
    if len(lst) < 2:
        return (-1, -1)
    
    start_index, finish_index = 0, 0
    element = lst[0]
    precipice = False
    indexs = []
    count = 0
    
    for el in range(len(lst)):
        if not precipice:
            if lst[el] >= element:
                element = lst[el]
            else:
                bigest_element = element
                smolest_element = lst[el]
                precipice = True
                if el == len(lst) -1:
                    if lst[el] < smolest_element:
                        smolest_element = lst[el]
                    finish_index = el
                    for e in range(len(lst)):
                        if lst[e] > smolest_element:
                            start_index = e
                            count += 1
                            break
                    indexs.append([start_index, finish_index])
                    precipice = False
        elif el == len(lst) - 1 and precipice == True:
            if lst[el] < smolest_element:
                smolest_element = lst[el]
            
            if lst[el] >= bigest_element:
                finish_index = el - 1
            else:
                finish_index = el
            element = lst[el]
            for e in range(len(lst)):
                if lst[e] > smolest_element:
                    start_index = e
                    count += 1
                    break
            indexs.append([start_index, finish_index])
            precipice = False
        else:
            if lst[el] >= bigest_element:
                finish_index = el - 1
                element = lst[el]
                for e in range(len(lst)):
                    if lst[e] > smolest_element:
                        start_index = e
                        count += 1
                        break
                indexs.append([start_index, finish_index])
                
                        
                precipice = False

                    
            elif lst[el] < smolest_element:
                smolest_element = lst[el]
        count += 1
    print(count)
    return indexs

def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort()
    
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        prev_start, prev_end = merged[-1]
        curr_start, curr_end = intervals[i]
        
        if curr_start <= prev_end:
            merged[-1] = [min(prev_start, curr_start), max(prev_end, curr_end)]
        else:
            merged.append([curr_start, curr_end])
    
    return merged
    
if __name__ == "__main__":
    lst = [randint(1, 100) for _ in range(100000)]
    print(lst)
    index = more_range_search(lst)
    result = merge_intervals(index)
    print(result)
