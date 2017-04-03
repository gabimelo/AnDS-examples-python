"""
@author Gabriela Melo
@since 04/03/2015
@modified 04/03/2015
@pre input is integer
@post temp_F is temperature in Farenheit
"""

temp_C = int(input('Enter temperature in Celsius '))

temp_F = int(9*temp_C/5 + 32)

print('Temperature in Fahrenheit is ' + str(temp_F))
