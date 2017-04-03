"""
@author Gabriela Melo
@since 08/04/2015
@modified 17/04/2015
"""

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


"""Task 1"""
size = int(input("Enter size of list: "))
the_list = []

for n in range(size):
    the_list.append(int(input("Enter next item of list: ")))

reverse(the_list)

print(the_list)

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

""" Task 2 """

num = int(input("Enter positive integer: "))

bin = binary(num)

print(bin)

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