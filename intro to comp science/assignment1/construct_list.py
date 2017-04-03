"""
@author Gabriela Melo
@since 04/03/2015
@modified 04/03/2015
@pre inputs are integers
@post the_list is list containing all input values
"""

size = int(input("Enter number of values: "))
the_list = []

for i in range(size):
    the_list.append(int(input("Value: ")))

print(the_list)
