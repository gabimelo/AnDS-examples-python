"""
@author Gabriela Melo
@since 14/05/2015
@modified 15/05/2015
"""
from task_3 import *

def find_word(my_list, word):
    array = []
    for i in range(len(my_list)):
            my_line = my_list.__str__(i)
            for j in range(len(my_line)):
                if my_line[j] == word[0]:
                    k = 1
                    j += 1
                    while j < len(my_line) and k < len(word) and my_line[j] == word[k]:
                        k += 1
                        j += 1
                    if k == len(word):
                        array.append(i)
    return array

def g(my_list, word):
    try:
        array = find_word(my_list, word)
        for i in array:
            line = my_list.__str__(i)
            print('Line number: ' + str(i) + '\nLine: ' + str(line))
    except:
       print('?') 

def s(my_list, word, new_word):
   try:
        array = find_word(my_list, word)
        for i in array:
            line = my_list.__str__(i)
            line = line.replace(str(word), str(new_word))
            my_list.delete(i)
            my_list.insert(line, i)
   except:
       print('?')  

def menu3():
    '''
    a modified version of task2's menu
    :return: None
    '''
    quit = False
    my_list = linked_list.LList()
    while not quit:
        commands = ['r', 'w', 'p', 'd', 'q', 'h', 'i', 'a', 'g', 's']
        string = input('Enter command: ')
        command = string.split(' ')[0]
        try:
            op = string.split(' ')[1]
        except IndexError:
            op = None
        try:
            op2 = string.split(' ')[2]
        except IndexError:
            op2 = None
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
                g word
                s word new_word
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
            elif command == 'g':
                g(my_list, op)
            elif command == 's':
                s(my_list, op, op2)

if __name__ == '__main__':
    menu3()
