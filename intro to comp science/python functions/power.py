"""
@param: base and exponent
@pre: binary and reverse are defined
@post: returns b**e
@complexity: best and worse case are the same: O(N) (because of reverse())
"""
def power(b, e):
	rev_binary = binary(e)
	reverse(rev_binary)

	result = 1
	idx = len(rev_binary) - 1
	while idx >= 0:
		result *= result

		if rev_binary[idx]:
			result *= b

		idx -= 1

	return result

"""
@param: none
@pre: power is defined
@post: returns True if power if functioning properly, False otherwise
@complexity: best and wort case are the same: O(1)
"""
def new_power():
	correct = True
	if power(4,2) != 16:
		correct = False
	if power(3,4) != 81:
		correct = False
	return correct