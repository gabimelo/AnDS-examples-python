"""
@param: base and exponent
@pre: none
@post: returns b**e
@complexity: ?????
"""
def bitwise_power(b, e):
    result = 1

    i = 1
    idx = 0
    while i&e != e:
        i = (i<<1) | 1
        idx += 1
    while idx >= 0:
        result *= result
        i = 1
        for n in range(idx):
            i = i<<1
        if (i&e != 0):
            result *= b

        idx -= 1

    return result


"""
@param: none
@pre: bitwise_power is defined
@post: returns True if bitwise_power if functioning properly, False otherwise
@complexity: best and wort case are the same: O(1)
"""
def bitwise_new_power():
	correct = True
	if power(4,2) != 16:
		correct = False
	if power(3,4) != 81:
		correct = False
	return correct