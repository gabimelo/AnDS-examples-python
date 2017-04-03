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