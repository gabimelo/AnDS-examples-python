"""
@author Gabriela Melo
@since 23/04/2015
@modified 01/05/2015
"""
import stack

def print_menu():
    print('\nMenu:')
    print('1. push')
    print('2. pop')
    print('3. print')
    print('4. size')
    print('5. quit')
    
my_stack = stack.Stack(40)
quit = False

while not quit:
    print_menu()
    
    command = input("\nEnter command: ")
    try:
        command = int(command)
    except ValueError:
        print("\nEnter integer corresponding to desired command")
    
    if command == 1:
        item = input("Enter integer: ")
        try:
            int(item)
            my_stack.push(item)
        except ValueError:
            print("Only integers allowed!")
    elif command == 2:
        item = my_stack.pop()
        print(item)
    elif command == 3:
        my_string = my_stack.__str__()
        print(my_string)
    elif command == 4:
        size = my_stack.__len__()
        print(size)
    elif command == 5:
        quit = True
    else:
        print("Please select from the following command options")
