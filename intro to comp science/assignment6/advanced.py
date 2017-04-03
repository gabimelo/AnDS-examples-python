"""
@author Gabriela Melo
@since 23/04/2015
@modified 01/05/2015
"""

""" 
@param: string to be returned in RPN, 
            string has to be in infix notation
@pre: find_type is defined, reverse_stack is defined 
        class Stack should be on the same folder location
@post: returns expression in a RPN stack
@complexity: best = worse = O(N)
"""
def infix_to_rpn(a_string):
    import stack
    my_stack = stack.Stack(40)
    temp_stack = stack.Stack(40)
    n = 0

    while n < len(a_string):
        temp = ""
        while n < len(a_string) and a_string[n] == " ":
            n += 1
        while n < len(a_string) and (temp == "" or find_type(a_string[n]) == item_type):
            temp += a_string[n]
            n += 1
            item_type = find_type(temp)
        while n < len(a_string) and a_string[n] == " ":
            n += 1
        n -= 1
        if item_type == 0:
        	my_stack.push(temp)
        if item_type == 1:
        	if temp_stack.is_empty():
        		temp_stack.push(temp)
        	elif (temp_stack.peek() == "+" or temp_stack.peek() ==  "-") and (temp == "*" or temp == "/"):
        		temp_stack.push(temp)
        	else:
        		while (not temp_stack.is_empty() and (temp_stack.peek() == "*" or temp_stack.peek() == "/")):
        			my_stack.push(temp_stack.pop())
        		temp_stack.push(temp)
        if item_type == 2:
            print("An item has invalid type")
        n += 1

    while not temp_stack.is_empty():
    	my_stack.push(temp_stack.pop())

    assert not my_stack.is_empty(), "Couldn't evaluate expression. Please enter valid infix expressions (numbers interposed with operators)"

    my_stack = reverse_stack(my_stack)
    return my_stack
    

"""
@param none
@pre class Stack is in the same folder location 
        and infix_to_rpn is defined
@post returns True if infix_to_rpn is working properly, 
            False if not
@complexity best = worse = O(1)
"""
def test_infix_to_rpn():
    correct = True
    import stack

    my_stack = stack.Stack(40)
    my_stack.push('+')
    my_stack.push(2)
    my_stack.push(1)
    rpn_stack = infix_to_rpn("1+2")
    if my_stack.__str__() != rpn_stack.__str__():
        correct = False

    my_stack = stack.Stack(40)
    my_stack.push('+')
    my_stack.push('*')
    my_stack.push(3)
    my_stack.push(2)
    my_stack.push(1)
    rpn_stack = infix_to_rpn("1+2*3")
    if my_stack.__str__() != rpn_stack.__str__():
        correct = False

    my_stack = stack.Stack(40)
    my_stack.push('+')
    my_stack.push('*')
    my_stack.push(3)
    my_stack.push(2)
    my_stack.push(1)
    rpn_stack = infix_to_rpn(" 1 + 2 *  3")
    if my_stack.__str__() != rpn_stack.__str__():
        correct = False

    correct = False
    try:
        rpn_stack = infix_to_rpn("*+")
    except AssertionError:
        correct = True

    return correct

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

def reverse_stack(a_stack):
    import stack
    temp = stack.Stack(a_stack.__len__())

    for n in range(a_stack.__len__()):
        temp.push(a_stack.pop())

    return temp


import stack

# quit = False

# while not quit:
#     my_string = str(input("Enter infix expression [q to quit]: "))
    
#     if my_string != 'q':
#         print("RPN expression: ", end = "")
#         my_stack = infix_to_rpn(my_string)
#         print(my_stack.__str__())
#     else:
#         quit = True

print(test_infix_to_rpn())