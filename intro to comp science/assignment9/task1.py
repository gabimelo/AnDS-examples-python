'''
@ author: Brian Ezra, Gabriela Melo
@ since: 15/05/2015
@ modified: 22/05/2015
'''

def qty_chars(file):
    '''
    counts the amount of characters in a plain text file
    :param file: a text file(.txt)
    :return: integer, positive or 0
    :complexity: O(1)
    '''
    f = open(file, 'r')
    qty = len(f.read())
    f.close()
    return qty

def write_letters(i_file, o_file):
    '''
    converts all the letters from an inputted file into lowercase and then writes it into an output file
    :param i_file: plain text file(.txt)
    :param o_file: plain text file(.txt)
    :return: None
    :complexity: O(N) where N = num of characters in input file
    '''    
    lc_letters = list(range(ord('a'), ord('z')+1))
    up_letters = list(range(ord('A'), ord('Z')+1))
    letters = up_letters + lc_letters
    string = ''

    f = open(i_file, 'r')
    my_str = f.read()
    f.close()

    for char in my_str:
        if (ord(char) in letters):
            if (ord(char) in up_letters):
                char = char.lower()
            string += char

    f = open(o_file, 'w')
    f.write(string)
    f.close()

from merge_sort import *

def letter_freq(file):
    '''
    prints the frequency table of each letter in a given file, with its frequency descending- sorted using merge_sort
    :param file: a plain text file(.txt)
    :return: prints a frequency table
    :complexity: O(num of letters in a file): most dominant
    '''
    write_letters(file, file)

    f = open(file, 'r')
    my_str = f.read()
    f.close()

    my_list = []

    for i in range(ord('a'), ord('z')+1):
        my_list.append([chr(i), 0])

    for char in my_str:
        my_list[ord(char) - 97][1] += 1

    my_list = merge_sort(my_list)
    my_list.reverse()

    string = ''
    for i in range(len(my_list)):
        string += str(my_list[i][0]) + ' ' + str(my_list[i][1]) + ' '

    return string