"""@param n = size of list to be created 
@pre none 
@post returns a list of size n of random real numbers between 0 and 1 
@complexity best and worst case are the same. Complexity is O(n)"""
def create_random_list(n):
    import random
    random.seed(None, 2)
    a_list = []
    for j in range(n):
        a_list.append(random.random())
    return a_list