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