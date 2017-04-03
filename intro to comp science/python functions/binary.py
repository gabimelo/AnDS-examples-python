"""
@param: positive integer to be returned in binary representation
@pre: reverse is defined
@post: returns a list with the binary representation of number passed as parameter
@complexity: 
"""
def binary(num):
	rev_binary = [0]*num

	aux = num
	while (aux > 0):
		i = 0
		while (2**i <= aux):
			i += 1

		aux -= 2**i
		
		rev_binary[i-1] = 1

	while rev_binary[len(rev_binary)-1] == 0:
		rev_binary.pop(len(rev_binary)-1)

	reverse(rev_binary)

	return(rev_binary)

"""
@param: none
@pre: binary is defined
@post: returns True if binary if functioning properly, False otherwise
@complexity: best and wort case are the same: O(1)
"""
def test_binary():
	correct = True
	if binary(16) != [1,0,0,0,0]:
		correct = False
	if binary(3) != [1,1]:
		correct = False
	return correct