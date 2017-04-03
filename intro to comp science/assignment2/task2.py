"""Task 2
@author Gabriela Melo
@since 06/03/2015
@modified 13/03/2015
"""

def print_menu():
    print('\nMenu:')
    print('1. append')
    print('2. sort')
    print('3. print')
    print('4. clear')
    print('5. reverse')
    print('6. pop')
    print('7. size')
    print('8. insert')
    print('9. find')
    print('10. quit')
    
my_list = []
quit = False
input_line = None

while not quit:
    print_menu()
    
    command = int(input("\nEnter command: "))
    
    if command == 1:
        item = input("Item? ")
        my_list.append(item)
    elif command == 2:
        my_list.sort()
    elif command == 3:
        print(my_list)

    elif command == 4:
        my_list.clear()
    elif command == 5:
        my_list.reverse()
    elif command == 6:
        my_list.pop()
        print(my_list)
    elif command == 7:
        print(len(my_list))
    elif command == 8:
        item = input("\nEnter item: ")
        pos = int(input("\nEnter position: "))
        my_list.insert(pos-1, item)
    elif command == 9:
        item = input("\nEnter item: ")
        if item in my_list:
            print(my_list.index(item))
        else:
            print('False')
    elif command == 10:
        quit = True
