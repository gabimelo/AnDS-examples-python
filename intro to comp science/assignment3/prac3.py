"""@author Gabriela Souza de Melo
@since 16/03/2015
@modified 16/03/2015"""

"""Task 1"""

"""@param a_list = list of real numbers
@pre items of the list are real numbers 
@post returns sum of all the items in the list or zero if it's empty
@complexity best and worst case are the same. Complexity is O(n)"""
def sum_items(a_list):
    sum = 0
    if (a_list):
        for i in range(len(a_list)):
            sum += a_list[i]
    return sum

"""@pre function sum_items is defined
@post returns True if sum_items is working properly, False if it's not
@complexity best and worst case are the same. Complexity is O(1)"""
def test_sum_items():
    list1 = [1,2,3,4,5]
    list2 = []
    correct = True
    if sum_items(list1) != 15:
        correct = False
    if sum_items(list2) != 0:
        correct = False
    return correct
	
if __name__ == "__main__":
    test_sum_items()
	
"""Task 2"""

"""@param a_list = list of real numbers
@pre items of the list are real numbers; sum_items is defined
@post returns time taken to call sum_items
@complexity best and worst case are the same. Complexity is O(n)"""
def time_sum_items(a_list):
    import time
    start = time.clock()
    sum = sum_items(a_list)
    taken = (time.clock() - start)
    return taken

"""@pre time_sum_items is defined
@post prints the time taken to call time_sum_items for each list size
@complexity best and worst case are the same. Complexity is O(n)"""
def table_time_sum_items():
    for n in range(10):
        a_list = create_random_list(2**(n+1))
        print(str(2**(n+1)) + "   " + str(time_sum_items(a_list)))


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

"""@pre function create_random_list is defined
@post returns True if create_random_list is working properly, False if it's not
@complexity best and worst case are the same. Complexity is O(1)"""
def test_create_random_list():
    a_list = create_random_list(10)
    correct = True
    if len(a_list) != 10:
        correct = False
    for n in range(len(a_list)):
        if a_list[n] < 0 or a_list[n] > 1:
            correct = False
    return correct

"""Task 3"""

"""@param a_list is a list of real numbers
@pre function swap is defined
@post sorts a_list
@complexity best case is when only 1 number is out of place. Complexity is O(n)
            worst case is when it is in reverse order. Complexity is O(n**2)"""
def shaker_sort(a_list):
    n = len(a_list)
    swaps = True
    while(swaps == True):
        swaps = False
        for j in range(n-1):
            if(a_list[j] > a_list[j+1]):
                swap(a_list, j, j+1)
                swaps = True
        for j in range(n-1, 1, -1):
            if(a_list[j] < a_list[j-1]):
                swap(a_list, j, j-1)
                swaps = True

"""@param a list, and the indexes for the two positions of the list to be swapped
@post the two referenced items are swapped on the list
@complexity best and worst case are the same: O(1)"""
def swap(a_list, pos1, pos2):
    temp = a_list[pos1]
    a_list[pos1] = a_list[pos2]
    a_list[pos2] = temp

"""@pre function shaker_sort is defined
@post returns True if shaker_sort is working properly, False if it's not
@complexity best and worst case are the same. Complexity is O(1)"""
def test_shaker_sort():
    correct = True
    a_list = [9,8,7,6,5,4,3,2,1]
    shaker_sort(a_list) 
    if a_list != [1,2,3,4,5,6,7,8,9]:
        correct = False
    a_list = [1,5,2,6,4,8,3,7,9]
    shaker_sort(a_list)
    if a_list != [1,2,3,4,5,6,7,8,9]:
        correct = False
    return correct

"""@param a list to be sorted
@pre function shaker_sort is defined
@post returns the time taken to call shaker_sort
@complexity same as shaker_sort:
            best case is when only 1 number is out of place. Complexity is O(n)
            worst case is when it is in reverse order. Complexity is O(n**2)"""
def time_shaker_sort(a_list):
    import time
    start = time.clock()
    shaker_sort(a_list)
    taken = (time.clock() - start)
    return taken

"""@pre functions shaker_sort, time_shaker_sort and create_random_list are defined
@post time to call shaker_sort for each n length of list is printed
@complexity same as time_shaker_sort:
            same as shaker_sort:
            best case is when only 1 number is out of place. Complexity is O(n)
            worst case is when it is in reverse order. Complexity is O(n**2)"""
def table_time_shaker_sort():
    for n in range(10):
        a_list = create_random_list(2**(n+1))
        print(str(2**(n+1)) + "   " + str(time_shaker_sort(a_list)))

"""@pre functions shaker_sort and time_shaker_sort are defined
@post average time to call shaker_sort for each n length of list is printed
@complexity same as time_shaker_sort:
            same as shaker_sort:
            best case is when only 1 number is out of place. Complexity is O(n)
            worst case is when it is in reverse order. Complexity is O(n**2)"""
def table_avg_time_shaker_sort():
    for n in range(10):
        sum = 0
        for i in range(100):
            a_list = create_random_list(2**(n+1))            
            sum += time_shaker_sort(a_list)
        print(str(2**(n+1)) + "   " + str(sum/100))
            
"""Advanced Question"""

"""@param a_list is a list of real numbers
@pre function sum_items is defined
@post a list with the values for i_min and i_max is returned
@complexity best and worst case are the same. Complexity = O(n**3)"""
def find_max_sum_interval(a_list):
    n = len(a_list)
    max_sum = a_list[0]
    i_min = i_max = 0
    for size_array in range(n):
        for begin_array in range(n-size_array):
            this_sum = sum_items(a_list[begin_array:begin_array+size_array+1])
            if this_sum > max_sum:
                max_sum = this_sum
                i_min = begin_array
                i_max = begin_array + size_array
    indices = [i_min, i_max]
    return indices

"""@pre function find_max_sum_interval is defined
@post returns True if find_max_sum_interval is working properly, False if it's not
@complexity best and worst case are the same. Complexity is O(1)"""
def test_find_max_sum_interval():
    correct = True
    a_list = [9,8,7,6,5,4,3,2,1]
    indices = find_max_sum_interval(a_list)
    if indices != [0,8]:
        correct = False
    a_list = [9,-8,7,-6,5,-4,3,-2,1]
    indices = find_max_sum_interval(a_list)
    if indices != [0,0]:
        correct = False
    a_list = [9,-8,7,6,5,-4,3,-2,1]
    indices = find_max_sum_interval(a_list)
    if indices != [0,4]:
        correct = False
    a_list = [-9,-8,-7]
    indices = find_max_sum_interval(a_list)
    if indices != [2,2]:
        correct = False
    return correct

"""@param a list of real numbers
@pre function find_max_sum_interval is defined
@post returns the time taken to call find_max_sum_interval
@complexity same as find_max_sum_interval:
            best and worst case are the same. Complexity = O(n**3)"""
def time_find_max_sum_interval(a_list):
    import time
    start = time.clock()
    find_max_sum_interval(a_list)
    taken = (time.clock() - start)
    return taken

"""@pre functions create_random_list and time_find_max_sum_interval are defined
@post time to call find_max_sum_interval for each n length of list is printed
@complexity same as time_find_max_sum_interval:
            same as find_max_sum_interval:
            best and worst case are the same. Complexity = O(n**3)"""
def table_avg_time_find_max_sum_interval():
    for n in range(10):
        sum = 0
        for i in range(100):
            a_list = create_random_list(2**(n+1))            
            sum += time_find_max_sum_interval(a_list)
        print(str(2**(n+1)) + "   " + str(sum/100))

"""Hall of Fame"""

"""@param a_list is a list of real numbers
@pre none
@post a list with the values for i_min and i_max is returned
@complexity best and worst case are the same. Complexity = O(n)"""
def quick_find_max_sum_interval(a_list):
    # we have to keep adding, until sum beggins negative. If sum is greater than maximum sum, we update the maximum sum and the index
    n = len(a_list)
    max_sum = a_list[0]
    i_max = i_min = this_sum = begin_array = 0
    for j in range(n):
        this_sum += a_list[j]
        if this_sum > max_sum:
            max_sum = this_sum
            i_max = j
            i_min = begin_array                        
        if this_sum < 0:
            this_sum = 0
            begin_array = j+1
    indices = [i_min, i_max]
    return indices

"""@pre function quick_find_max_sum_interval is defined
@post returns True if quik_find_max_sum_interval is working properly, False if it's not
@complexity best and worst case are the same. Complexity is O(1)"""
def test_quick_find_max_sum_interval():
    correct = True
    a_list = [9,8,7,6,5,4,3,2,1]
    indices = quick_find_max_sum_interval(a_list)
    if indices != [0,8]:
        correct = False
    a_list = [9,-8,7,-6,5,-4,3,-2,1]
    indices = quick_find_max_sum_interval(a_list)
    if indices != [0,0]:
        correct = False
    a_list = [9,-8,7,6,5,-4,3,-2,1]
    indices = quick_find_max_sum_interval(a_list)
    if indices != [0,4]:
        correct = False
    a_list = [-9,-8,-7]
    indices = quick_find_max_sum_interval(a_list)
    if indices != [2,2]:
        correct = False
    return correct

"""@param a list of real numbers
@pre function quick_find_max_sum_interval is defined
@post returns the time taken to call uick_find_max_sum_interval
@complexity same as quick_find_max_sum_interval:
            best and worst case are the same. Complexity = O(n)"""
def time_quick_find_max_sum_interval(a_list):
    import time
    start = time.clock()
    quick_find_max_sum_interval(a_list)
    taken = (time.clock() - start)
    return taken

"""@pre functions create_random_list and time_quick_find_max_sum_interval are defined
@post average time to call quick_find_max_sum_interval for each n length of list is printed
@complexity same as time_quick_find_max_sum_interval:
            same as quick_find_max_sum_interval:
            best and worst case are the same. Complexity = O(n)"""
def table_avg_time_quick_find_max_sum_interval():
    for n in range(10):
        sum = 0
        for i in range(100):
            a_list = create_random_list(2**(n+1))            
            sum += time_quick_find_max_sum_interval(a_list)
        print(str(2**(n+1)) + "   " + str(sum/100))