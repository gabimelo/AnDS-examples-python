'''
@ author: Brian Ezra, Gabriela Melo
@ since: 11/05/2015
@ modified: 13/05/2015
'''

from task_3 import *

def test_read():
    correct = True
    my_list = linked_list.LList()
    my_list.append("Line 1\n")
    my_list.append("Line 2\n")
    my_list.append("Line 3\n")
    test = linked_list.LList()
    read(test, "test.txt")
    if my_list.__str__() != test.__str__():
        correct = False

    return correct

def test_write():
    correct = True
    my_list = linked_list.LList()
    test = linked_list.LList()
    read(my_list, "test.txt")
    write(my_list, "empty.txt")
    read(test, "empty.txt")
    if my_list.__str__() != test.__str__():
        correct = False

    return correct

def test_print():
    correct = False
    try:
        a_list.__print__()
    except:
        correct = True

    test = linked_list.LList()
    test.append("Line 1\n")
    correct = False
    try:
        test.__print__(10)
    except:
        correct = True
    
    return correct

def test_delete():
    correct = False
    test = linked_list.LList()
    try:
        delete(test, 4)
    except:
        correct = True
    correct = False
    try:
        delete(test, -4)
    except:
        correct = True
    correct = False
    try:
        delete(test, 'aasf')
    except:
        correct = True
    
    correct = True
    my_list = linked_list.LList()
    my_list.append("Line 1\n")
    my_list.append("Line 2\n")
    my_list.append("Line 3\n")
    test = linked_list.LList()
    test.append("Line 1\n")
    test.append("Line 2\n")
    test.append("Line 3\n")
    test.append("Line 4\n")

    delete(test, 3)
    if my_list.__str__() != test.__str__():
        correct = False

    my_list = linked_list.LList()
    my_list.append("Line 1\n")
    my_list.append("Line 2\n")
    delete(test, -1)
    if my_list.__str__() != test.__str__():
        correct = False
    
    my_list = linked_list.LList()
    delete(test)
    if my_list.__str__() != test.__str__():
        correct = False

    return correct

def test_insert():
    correct = False
    try:
        insert(test, 'aasf')
    except:
        correct = True
    
    correct = True
    my_list = linked_list.LList()
    my_list.append("Line 1\n")
    my_list.append("Line 2\n")
    test = linked_list.LList()
    test.append("Line 2\n")
    test.insert("Line 1\n", 0)
    if my_list.__str__() != test.__str__():
        correct = False

    my_list = linked_list.LList()
    my_list.append("Line 1\n")
    my_list.append("Line 2\n")
    my_list.append("Line 3\n")
    test = linked_list.LList()
    test.append("Line 1\n")
    test.append("Line 3\n")
    test.insert("Line 2\n", -1)
    if my_list.__str__() != test.__str__():
        correct = False
    
    my_list = linked_list.LList()
    my_list.append("Line 1\n")
    my_list.append("Line 2\n")
    test = linked_list.LList()
    test.append("Line 2\n")
    test.insert("Line 1\n", -10)
    if my_list.__str__() != test.__str__():
        correct = False

    my_list = linked_list.LList()
    my_list.append("Line 1\n")
    my_list.append("Line 2\n")
    test = linked_list.LList()
    test.append("Line 1\n")
    test.insert("Line 2\n", 10)
    if my_list.__str__() != test.__str__():
        correct = False

    return correct

if not test_read():
    print("Read not working!")
elif not test_write():
    print("Write not working!")
elif not test_print():
    print("Print not working!")
elif not test_delete():
    print("Delete not working!")
elif not test_insert():
    print("Insert not working!")
else:
    print("All functions are working!")