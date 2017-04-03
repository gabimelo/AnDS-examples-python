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