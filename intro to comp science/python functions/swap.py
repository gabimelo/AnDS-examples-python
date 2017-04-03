"""
@param: list, and position of items to be swaped
@pre: none
@post: list has the two items swaped
@complexity: best and worst case are the same: O(1)
"""
def swap(a_list, pos1, pos2):
    temp = a_list[pos1]
    a_list[pos1] = a_list[pos2]
    a_list[pos2] = temp