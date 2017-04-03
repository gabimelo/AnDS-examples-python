"""
@param: year to be tested for leap year
@pre: year >= 1582 
@post: returns True if it's a leap year, False otherwise
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