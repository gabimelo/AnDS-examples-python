'''
@ author: Brian Ezra, Gabriela Melo
@ since: 11/05/2015
@ modified: 13/05/2015
'''

import linked_list

def read(my_list, filename):
    '''
    opens a file, reads and put every line into a list, and closes it
    :param filename: string(with file extension, e.g. test.txt)
    :return: instance of the Linked List class
    :complexity: O(num of lines in filename)
    '''
    try:
        f = open(filename, 'r')
        for line in f:
            my_list.append(line)
        f.close()
    except:
        print('?')


def write(my_list, filename):
    '''
    writes the elements of a list onto a file
    :param filename: string
    :param my_list: a list object
    :return: None
    :complexity: O(1)
    '''
    try:
        f = open(filename, 'w')
        my_string = my_list.__str__()
        f.write(my_string)
        f.close()
    except:
        print('?')


def print_list(my_list, num=None):
    '''
    prints the content(s) of the list(see file linked list)
    :param my_list: a list object
    :param num: integer between -listlength and listlength
    :return: prints the list's content(s)
    '''
    try:
        my_list.__print__(num)
    except:
        print('?')


def delete(my_list, num=None):
    '''
    delete an item(see file linked list)
    :param my_list: object list
    :param num: integer between - length and length
    :return: None
    '''
    try:
        my_list.delete(num)
    except:
        print('?')


def menu():
    quit = False
    my_list = linked_list.LList()
    while not quit:
        commands = [0, 1, 2, 3, 4]
        print(
            '''
            ---Linked List class menu---
            Available commands:
            1. read
            2. write
            3. print
            4. delete
            0. quit
            '''
            )
        try:
            command = int(input('Input command: '))
        except ValueError:
            print('Command not an integer, try again')
        else:
            try:
                assert command in commands
            except AssertionError:
                print('Unknown command, try again')
            else:
                if command == 1:
                    filename = input('Enter filename: ')
                    read(my_list, filename)
                elif command == 2:
                    filename = input('Enter filename: ')
                    write(my_list, filename)
                elif command == 3:
                    num = input('Input index of line to print (can be empty): ')
                    print_list(my_list, num)
                elif command == 4:
                    num = input('Input index of line to delete (can be empty): ')
                    delete(my_list, num)
                elif command == 0:
                    quit = True


if __name__ == '__main__':
    menu()
