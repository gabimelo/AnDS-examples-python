def merge_sort(a_list):
	'''
    merge part of the merge sort, uses built in list
    :param left: list of list
    :param right: list of list
    :return: sorted list
    :complexity: O(N logN): where N is len(a_list)
    '''
	if len(a_list) <= 1:
		return a_list
	first_part = a_list[:len(a_list)//2]
	second_part = a_list[(len(a_list)//2):]

	first_part = merge_sort(first_part)
	second_part = merge_sort(second_part)

	return combine(first_part, second_part)

def combine(first_part, second_part):
	'''
    combines in ascend-sort the given lists
    :param two lists to be merged
    :return: sorted list
    :complexity: O(N) : logN from splitting the list, N from merge
    '''
	temporary = [None] * (len(first_part)+len(second_part))
	j = k = 0

	for i in range(len(temporary)):
		if j < len(first_part) and (k >= len(second_part) or first_part[j] < second_part[k]):
			temporary[i] = first_part[j]
			j += 1
		elif k < len(second_part) and (j >= len(first_part) or first_part[j] > second_part[k]):
			temporary[i] = second_part[k]
			k += 1
	
	return temporary