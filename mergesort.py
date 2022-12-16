
def merge_sort(unsorted_list):
    n = len(unsorted_list)
    if n <= 1:
        return unsorted_list
    midpoint = n // 2
    left_list, right_list = merge_sort(unsorted_list[:midpoint]), merge_sort(unsorted_list[midpoint:])
    l_pointer, r_pointer = 0, 0
    result_list = []
    while l_pointer < midpoint or r_pointer < n - midpoint:
        if l_pointer == midpoint:
            result_list.append(right_list[r_pointer])
            r_pointer += 1
        elif r_pointer == n - midpoint:
            result_list.append(left_list[l_pointer])
            l_pointer += 1
        elif left_list[l_pointer] < right_list[r_pointer]:
            result_list.append(left_list[l_pointer])
            l_pointer += 1
        else:
            result_list.append(right_list[r_pointer])
            r_pointer += 1
    return result_list

print(merge_sort([2, 1, 5, 7 -1]))
        
