""" 
@param: stack containing expression in RPN
@pre: stack has to contain numbers and operands (+,-,*,/) 
      and be an expression in RPN notation, 
      class Stack is in same folder location,
      find_type is defined
@post: returns result of expression
@complexity: best = worse = O(N)
"""
def evaluate(my_stack):
    import stack
    result_stack = stack.Stack(40)

    while not my_stack.is_empty():
        item_type = 1
        while item_type != 0 and not my_stack.is_empty():
            item1 = str(my_stack.pop())
            item_type = find_type(item1)
            if item_type == 1:
                item_type = 0
                my_stack.push(item1)
                if not result_stack.is_empty():
                    item1 = result_stack.pop()
        
        try:    
            item1 = int(item1)
        except ValueError:
            print("Missing operand")
        
        item_type = 1
        while item_type != 0 and not my_stack.is_empty():
            item2 = str(my_stack.pop())
            item_type = find_type(item2)
            if item_type == 1:
                my_stack.push(item2)
                item_type = 0
                if not result_stack.is_empty():
                    item2 = item1
                    item1 = result_stack.pop()
        
        try:    
            item2 = int(item2)
        except ValueError:
            print("Missing operand")

        item_type = 0
        while item_type != 1 and not my_stack.is_empty():
            op = str(my_stack.pop())
            item_type = find_type(op)
            if item_type == 0:
                result_stack.push(item1)
                item1 = item2
                item2 = int(op)
            elif item_type == 2:
                print("An item is of invalid type")
        
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
            assert item2 != 0, "Can't divide by zero."
            result = item1 / item2
            op = ""
    
        result_stack.push(result)

    return result_stack.pop()

"""
@param none
@pre evaluate is defined, class Stack should be on the same folder location
@post returns True if evaluate is working properly, 
            False if not
@complexity best = worse = O(1)
""" 
def test_evaluate():
    import stack
    correct = True

    # testing 1 + 2/3
    a_stack = stack.Stack(40)
    a_stack.push('+')
    a_stack.push('/')
    a_stack.push(3)
    a_stack.push(2)
    a_stack.push(1)
    if (1 + 2/3) != evaluate(a_stack):
        correct = False

    # testing (1 + 2)/3
    a_stack = stack.Stack(40)
    a_stack.push('/')
    a_stack.push(3)
    a_stack.push('+')
    a_stack.push(2)
    a_stack.push(1)
    if ((1 + 2)/3) != evaluate(a_stack):
        correct = False

    # testing 1/2 + 3
    a_stack = stack.Stack(40)
    a_stack.push('+')
    a_stack.push(3)
    a_stack.push('/')
    a_stack.push(2)
    a_stack.push(1)
    if (1/2 + 3) != evaluate(a_stack):
        correct = False

    # testing 1/(2 + 3)
    a_stack = stack.Stack(40)
    a_stack.push('/')
    a_stack.push('+')
    a_stack.push(3)
    a_stack.push(2)
    a_stack.push(1)
    if (1/(2 + 3)) != evaluate(a_stack):
        correct = False

    # testing (1 + 2)/(3 - 4)
    a_stack = stack.Stack(40)
    a_stack.push('/')
    a_stack.push('-')
    a_stack.push(4)
    a_stack.push(3)
    a_stack.push('+')
    a_stack.push(2)
    a_stack.push(1)
    if ((1 + 2)/(3 - 4)) != evaluate(a_stack):
        correct = False

    # testing (1 + 2)*(3 - 4)/(5 + 6)
    a_stack = stack.Stack(40)
    a_stack.push('/')
    a_stack.push('+')
    a_stack.push(6)
    a_stack.push(5)
    a_stack.push('*')
    a_stack.push('-')
    a_stack.push(4)
    a_stack.push(3)
    a_stack.push('+')
    a_stack.push(2)
    a_stack.push(1)
    if (-3/11) != evaluate(a_stack):
        correct = False

    # test if can handle expressions without operands
    a_stack.push(3)
    a_stack.push(2)
    a_stack.push(1) 
    correct = False
    try:
        evaluate(a_stack)
    except AssertionError:
        correct = True
    
    # test if can handle expressions without numbers
    a_stack.push('+')
    a_stack.push('-')
    a_stack.push('/') 
    correct = False
    try:
        evaluate(a_stack)
    except AssertionError:
        correct = True

    # test if can handle expressions without numbers
    a_stack.push('/')
    a_stack.push(0)
    a_stack.push(1) 
    correct = False
    try:
        evaluate(a_stack)
    except AssertionError:
        correct = True

    return correct