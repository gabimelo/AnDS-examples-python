""" 
@param: string to be returned in RPN, 
            string has to be in infix notation, 
            but may have parenthesis
@pre: find_type is defined, reverse_stack is defined 
        class Stack should be on the same folder location
@post: returns expression in a RPN stack
@complexity: best = worse = O(N)
"""
def smart_infix_to_rpn(a_string):
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
            if temp_stack.is_empty() or temp_stack.peek() == '(':
                temp_stack.push(temp)
            elif (temp_stack.peek() == "+" or temp_stack.peek() ==  "-") and (temp == "*" or temp == "/"):
                temp_stack.push(temp)
            else:
                while (not temp_stack.is_empty() and (temp_stack.peek() == "*" or temp_stack.peek() == "/")):
                    my_stack.push(temp_stack.pop())
                temp_stack.push(temp)
        if item_type == 3:
            if temp == '(':
                temp_stack.push(temp)
            elif temp == ')':
                while temp_stack.peek() != '(':
                    my_stack.push(temp_stack.pop())
                temp_stack.pop()
        if item_type == 2:
            print("An item has invalid type")
        n += 1

    while not temp_stack.is_empty():
        my_stack.push(temp_stack.pop())

    assert not my_stack.is_empty(), "Couldn't evaluate expression. Please enter valid infix expressions (numbers interposed with operators and parenthesis)"

    my_stack = reverse_stack(my_stack)
    return my_stack

"""
@param none
@pre class Stack is in the same folder location 
        and smart_infix_to_rpn is defined
@post returns True if smart_infix_to_rpn is working properly, 
            False if not
@complexity best = worse = O(1)
"""
def test_smart_infix_to_rpn():
    correct = True
    import stack

    # testing 1 + 2/3
    rpn_stack = smart_infix_to_rpn(" 1 + 2/3 ")
    if ('1 2 3 / +') != rpn_stack.__str__():
        correct = False

    # testing 1 + 2/3
    rpn_stack = smart_infix_to_rpn(" 1 + (2/3) ")
    if ('1 2 3 / +') != rpn_stack.__str__():
        correct = False

    # testing (1 + 2)/3
    rpn_stack = smart_infix_to_rpn("(1 + 2)/3")
    if ('1 2 + 3 /') != rpn_stack.__str__():
        correct = False 

    # testing ***
    correct = False
    try:
        rpn_stack = smart_infix_to_rpn("*+")
        print(rpn_stack.__str__())
    except AssertionError:
        correct = True

    return correct