"""
@param: m and n, two numbers from which the pythagorian triple is going to be generated
@pre: none 
@post: returns pythagorian triple constructed from user's inputs
@complexity: best and worst case are the same: O(1)
"""
def pythagorian(m, n):
	import math

	a = int(math.fabs(m**2 - n**2))
	b = 2 * m * n
	c = m**2 + n**2

	return a, b, c

"""
@param: none
@pre: function pythagorian is defined 
@post: returns True if pythagorian is working properly, False if it's not
@complexity: best and worst case are the same: O(n)
"""
def test_pythagorian():
	correct = True
	if pythagorian(2,1) != (3,4,5):
		correct = False
	if pythagorian(3,2) != (5,12,13):
		correct = False
	if correct == True:
		print("pythagorian(m, n) is working properly!")
	else:
		print("pythagorian(m, n) is not working properly!")