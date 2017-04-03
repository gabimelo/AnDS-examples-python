"""@param a_list is a list of real numbers
@pre function sum_items is defined
@post a list with the values for i_min and i_max is returned
@complexity best and worst case are the same. Complexity = O(n**3)"""
def find_max_sum_interval(a_list):
    n = len(a_list)
    max_sum = a_list[0]
    i_min = i_max = 0
    for size_array in range(n):
        for begin_array in range(n-size_array):
            this_sum = sum_items(a_list[begin_array:begin_array+size_array+1])
            if this_sum > max_sum:
                max_sum = this_sum
                i_min = begin_array
                i_max = begin_array + size_array
    indices = [i_min, i_max]
    return indices