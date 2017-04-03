"""@param a_list is a list of real numbers
@pre none
@post a list with the values for i_min and i_max is returned
@complexity best and worst case are the same. Complexity = O(n)"""
def quick_find_max_sum_interval(a_list):
    # we have to keep adding, until sum beggins negative. If sum is greater than maximum sum, we update the maximum sum and the index
    n = len(a_list)
    max_sum = a_list[0]
    i_max = i_min = this_sum = begin_array = 0
    for j in range(n):
        this_sum += a_list[j]
        if this_sum > max_sum:
            max_sum = this_sum
            i_max = j
            i_min = begin_array                        
        if this_sum < 0:
            this_sum = 0
            begin_array = j+1
    indices = [i_min, i_max]
    return indices