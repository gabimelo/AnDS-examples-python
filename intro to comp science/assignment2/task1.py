"""Task 1
@author Gabriela Melo
@since 06/03/2015
@modified 13/03/2015

modifications:
1- flag has to be initialized
2- for If statements, equal condition is stated with == and not =
3- booleans True and False have to have first letter capitalized
4- if it's 0 or 1 it's not prime, but doesn't follow the 
   general rule, therefore, wouldn't be indicated as not 
   primes on the general check. Hence, they have to be 
   checked separately
5- case n=9 needs to be checked, therefore we need k*k <= n
6- loop is infinite if k is not incremented by the end of it
"""

def is_prime(n):
    k = 3
    
    flag = True
	    
    if (n == 2):
        flag = True
    elif (n == 0 or n == 1 or n % 2 == 0):
        flag = False
    else:
        while (k*k <= n):
            if (n % k == 0):
                flag = False
                break
            k += 1
    return flag

n = int(input('Please enter positive integer: '))

for i in range(n):
    if (is_prime(i)):
        print(i)
