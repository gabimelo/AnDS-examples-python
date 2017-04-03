"""
@author Gabriela Melo
@since 04/03/2015
@modified 04/03/2015
@pre input is integer
"""

year = int(input('Enter year: '))

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print(year, 'is a leap year')
else:
    print(year, 'is NOT a leap year')
