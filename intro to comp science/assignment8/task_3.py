'''
@ author: Brian Ezra, Gabriela Melo
@ since: 11/05/2015
@ modified: 13/05/2015
'''
from task_2 import *

def insertLines(my_list, index):
    '''
    insert multiple items in a list. Each line is an item
    :param my_list: object list
    :param index: integer
    :return: None
    '''
    try:
        index = int(index)
        item = input('Enter lines: ') + '\n'
        while item != '.\n':
            my_list.insert(item, index)
            index += 1
            item = input() + '\n'
    except ValueError:
        print('?')

def appendLines(my_list):
    '''
    append multiple items in a list. Each line is an item
    :param my_list: object list
    :return: None
    '''
    item = input('Enter lines: ') + '\n'
    while item != '.\n':
        my_list.append(item)
        item = input() + '\n'

def menu2():
    '''
    a modified version of task2's menu
    :return: None
    '''
    quit = False
    my_list = linked_list.LList()
    while not quit:
        commands = ['r', 'w', 'p', 'd', 'q', 'h', 'i', 'a']
        string = input('Enter command: ')
        command = string.split(' ')[0]
        try:
            op = string.split(' ')[1]
        except IndexError:
            op = None
        try:
            assert command in commands
        except AssertionError:
            print('Unknown command, try again')
        else:
            if command == 'h':
                print(
                '''
                ---Linked List class menu---
                Available commands:
                r filename
                w filename
                p num
                d num
                i num
                a
                q
                '''
                )
            elif command == 'r':
                read(my_list, op)
            elif command == 'w':
                write(my_list, op)
            elif command == 'p':
                print_list(my_list, op)
            elif command == 'd':
                delete(my_list, op)
            elif command == 'q':
                quit = True
            elif command == 'i':
                insertLines(my_list, op)
            elif command == 'a':
                appendLines(my_list)

if __name__ == '__main__':
    menu2()
