"""
@author Gabriela Melo
@since 23/04/2015
@modified 01/05/2015
"""

""" 
@param: string to be split, with each piece separated by blank space
@pre: string has to have no more than 40 pieces, 
        class Stack should be on the same folder location
@post: returns a stack with each piece of string as 
        an item. Last piece of string is on top
@complexity: best = worse = O(N)
"""
def split(a_string):
    import stack
    my_stack = stack.Stack(40)
    n = 0

    while n < len(a_string):
        temp = ""
        while n < len(a_string) and a_string[n] == " ":
            n += 1
        while n < len(a_string) and a_string[n] != " ":
            temp += a_string[n]
            n += 1
        while n < len(a_string) and a_string[n] == " ":
            n += 1
        try:
            my_stack.push(temp)
        except AssertionError:
            print("Could not get all parts of string. String should have no more than 40 pieces.")
            n = len(a_string)

    return my_stack

"""
@param none
@pre split is defined, class Stack should be on the same folder location
@post returns True if split is working properly, 
            False if not
@complexity best = worse = O(1)
"""      
def test_split():
    import stack
    correct = True
    a_string = "a b c d e"
    a_stack = split(a_string)
    if "e d c b a" != a_stack.__str__():
        correct = False
    a_string = "   a   b   c    "
    a_stack = split(a_string)
    if "c b a" != a_stack.__str__():
        correct = False
    a_string = "a b c d e a b c d e a b c d e a b c d e a b c d e a b c d e a b c d e a b c d e a b c d e"
    a_stack = split(a_string)
    if "e d c b a e d c b a e d c b a e d c b a e d c b a e d c b a e d c b a e d c b a" != a_stack.__str__():
        correct = False
    return correct

""" 
@param: stack to be put in reverse order
@pre: stacks can't have more than 40 items, class Stack should be on the same folder location
@post: returns reversed stack
@complexity: best = worse = O(N)
"""
def reverse_stack(a_stack):
    import stack
    temp = stack.Stack(a_stack.__len__())

    for n in range(a_stack.__len__()):
        temp.push(a_stack.pop())

    return temp

"""
@param none
@pre reverse_stack is defined, class Stack should be on the same folder location
@post returns True if split is working properly, 
            False if not
@complexity best = worse = O(1)
""" 
def test_reverse_stack():
    correct = True
    import stack
    a_stack = stack.Stack(40)
    a_stack.push(1)
    a_stack.push(2)
    a_stack.push(3)
    a_stack = reverse_stack(a_stack)
    if "1 2 3" != a_stack.__str__():
        correct = False
    a_stack = stack.Stack(40)
    a_stack.push(1)
    a_stack.push(2)
    a_stack.push(3)
    a_stack.push('a')
    a_stack.push('b')
    a_stack.push('!')
    a_stack = reverse_stack(a_stack)
    if "1 2 3 a b !" != a_stack.__str__():
        correct = False
    return correct

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
        if item == "+" or item == "-" or item == "*" or item == "/" or item == "=":
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

""" 
@param: item to be described
@pre: find_type is defined
@post: none
@complexity: best = worse = O(1)
"""
def describe(item):
    item_type = find_type(item)
    if len(item) < 6:
        n = 6 - len(item)
        for i in range(n):
            print(" ", end="")
    print(item, end = "")
    if item_type == 0:
        print(" Integer")
    if item_type == 1:
        print(" Operator")
    if item_type == 2:
        print(" Invalid string")

my_string = str(input("Enter a string: "))

my_stack = split(my_string)

my_stack = reverse_stack(my_stack)

for n in range(my_stack.__len__()):
    describe(str(my_stack.pop()))