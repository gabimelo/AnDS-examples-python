"""@param a_list = list of real numbers
@pre items of the list are real numbers 
@post returns sum of all the items in the list or zero if it's empty
@complexity best and worst case are the same. Complexity is O(n)"""
def sum_items(a_list):
    sum = 0
    if (a_list):
        for i in range(len(a_list)):
            sum += a_list[i]
    return sum