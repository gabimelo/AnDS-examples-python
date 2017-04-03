"""
@param: list to be put in reverse order
@pre: swap() is defined
@post: list is in reverse order
@complexity: best and wort case are the same: O(N)
"""
def reverse(the_list):
    size = len(the_list)
    import math
    for n in range(math.floor(size/2)):
        swap(the_list, n, size-n-1)

"""
@param: none
@pre: reverse is defined
@post: returns True if reverse if functioning properly, False otherwise
@complexity: best and wort case are the same: O(1)
"""
def test_reverse():
	correct = True
	the_list = [1,2,3]
	reverse(the_list)
	if the_list != [3,2,1]:
		correct = False
	the_list = [1,2]
	reverse(the_list)
	if the_list != [2,1]:
		correct = False
	return correct