import linkedList

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
        item = input() + '\n'\

def find_word(my_list, word):
    '''
    return array with the indexes for the lines where word can be found
    my_list is linked list where each item is one line
    '''
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
    '''
    prints lines where word is found
    '''
    try:
        array = find_word(my_list, word)
        for i in array:
            line = my_list.__str__(i)
            print('Line number: ' + str(i) + '\nLine: ' + str(line))
    except:
       print('?') 

def s(my_list, word, new_word):
    '''
    replaces every occurence of word with new_word
    my_list is linked list where each item is one line
    '''
   try:
        array = find_word(my_list, word)
        for i in array:
            line = my_list.__str__(i)
            line = line.replace(str(word), str(new_word))
            my_list.delete(i)
            my_list.insert(line, i)
   except:
       print('?')  