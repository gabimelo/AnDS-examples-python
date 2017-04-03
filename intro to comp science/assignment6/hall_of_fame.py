"""
@author Gabriela Melo
@since 23/04/2015
@modified 01/05/2015
"""

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

def find_type(item):
    try:
        item = int(item)
        item_type = 0
    except:
        if item == "+" or item == "-" or item == "*" or item == "/" or item == "=":
            item_type = 1
        elif item == "(" or item == ")":
            item_type = 3
        else:
            item_type = 2
    return item_type

def reverse_stack(a_stack):
    import stack
    temp = stack.Stack(40)

    for n in range(a_stack.__len__()):
        item = a_stack.pop()
        temp.push(item)

    return temp

def evaluate(my_stack):
    import stack
    result_stack = stack.Stack(40)

    while not my_stack.is_empty():
        wrong = True
        while wrong and not my_stack.is_empty():
            wrong = False
            item1 = str(my_stack.pop())
            item_type = find_type(item1)
            if item_type == 1:
                my_stack.push(item1)
                if not result_stack.is_empty():
                    item1 = result_stack.pop()
            elif item_type == 2:
                wrong = True
            else:
                item1 = int(item1)
        
        wrong = True
        while wrong and not my_stack.is_empty():
            wrong = False
            item2 = str(my_stack.pop())
            item_type = find_type(item2)
            if item_type == 1:
                my_stack.push(item2)
                if not result_stack.is_empty():
                    item2 = item1
                    item1 = result_stack.pop()
            elif item_type == 2:
                wrong = True
            else:
                item2 = int(item2)

        wrong = True
        while wrong and not my_stack.is_empty():
            wrong = False
            op = str(my_stack.pop())
            item_type = find_type(op)
            if item_type == 0:
                result_stack.push(item1)
                item1 = item2
                item2 = int(op)
                wrong = True
            elif item_type == 2:
                print("An item is of invalid type")
                wrong = True
        
        assert find_type(op) == 1 and find_type(item1) == 0 and find_type(item2) == 0, "Missing operand and/or operator"

        if op == "+":
            result = item1 + item2
            op = ""
        elif op == "-":
            result = item1 - item2
            op = ""
        elif op == "*":
            result = item1 * item2
            op = ""
        elif op == "/":
            result = item1 / item2
            op = ""
    
        result_stack.push(result)

    return result_stack.pop()

my_string = str(input("Enter infix expression: "))
my_stack = smart_infix_to_rpn(my_string)
print(evaluate(my_stack))
