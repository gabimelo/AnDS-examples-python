"""
@author Gabriela Melo
@since 23/03/15
@modified 27/03/15
"""

#Task 1: pythagorian.py
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

#Task 2: isLeapYear.py

"""
@param: year to be tested for leap year
@pre: year >= 1582 
@post: prints "Is a leap year" if inputed item is a leap year
	   if not, prints "Is not a leap year"
@complexity: best and worst case are the same: O(1)
"""
def isLeapYear(year):
	leap = False

	if year % 4 == 0:
		if year % 100 != 0:
			leap = True

	if year % 400 == 0:
		leap = True

	return leap

"""
@param: none 
@pre: function isLeapYear is defined 
@post: returns True if isLeapYear is working properly, False if it's not
@complexity: best and worst case are the same: O(n)
"""
def test_isLeapYear():
	correct = True
	if isLeapYear(2016) != True:
		correct == False
	if isLeapYear(2015) != False:
		correct == False
	if correct == True:
		print("isLeapYear is working properly!")
	else:
		print("isLeapYear is not working properly!")


print("Enter two numbers: ")
m = int(input())
n = int(input())

test_pythagorian()

a, b, c = pythagorian(m, n)
print("Your pythagorian triple is: (" + str(a) + ", " + str(b) + ", " + str(c) + ")")

print("Enter a year (greater than 1582): ")
year = int(input())

test_isLeapYear()

result = isLeapYear(year)

if result == True:
	print("Is a leap year")
else:
	print("Is not a leap year")
