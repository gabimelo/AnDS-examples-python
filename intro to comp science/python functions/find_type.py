""" 
@param: item to have its type found
@pre: none
@post: returns 0 if its an integer, 1 if it's an operator(+,-,*,/,=), else 2
@complexity: best = worse = O(1)
"""
def find_type(item):
    try:
        item = int(item)
        item_type = 0
    except:
        if item in ("+", "-", "*", "/", "="):
            item_type = 1
        else:
            item_type = 2
    return item_type

"""
@param none
@pre find_type is defined
@post returns True if find_type is working properly, 
            False if not
@complexity best = worse = O(1)
""" 
def test_find_type():
    correct = True
    if 0 != find_type('1'):
        correct = False
    if 1 != find_type('+'):
        correct = False
    if 2 != find_type('+sa'):
        correct = False
    return correct