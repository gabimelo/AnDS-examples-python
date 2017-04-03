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


'''
@ author: Brian Ezra, Gabriela Melo
@ since: 15/05/2015
@ modified: 22/05/2015
'''

from task1 import *
from task2 import *

def write_ascii(i_file, o_file):
    '''
    writes the ascii representation for each character in i_file into o_file
    param i_file: input filename
    param o_file: output filename
    pre: write_letters must be defined
    post: o_file has a single binary string
    complexity: O(N), where N = number of letters in i_file
    '''
    write_letters(i_file, i_file)

    f = open(i_file, 'r')
    my_str = f.read()
    f.close()

    string = ''
    for char in my_str:
        string += str(bin(ord(char)))
    
    f = open(o_file, 'w')   
    f.write(string)
    f.close()

def construct_tree():
    '''
    a Binary Tree is constructed, where each letter is a node and their address is their ascii code
    pre: BinaryTree must be defined
    return: binary tree 
    complexity: O(1)
    '''
    tree = BinaryTree()

    lc_letters = list(range(ord('a'), ord('z')+1))

    string = ''

    for char in lc_letters:
        tree.add(chr(char), bin(char)[2:])

    return tree

def write_chars(i_file, o_file):
    '''
    writes in o_file the letter for each ascii binary number in i_file
    param i_file: input filename
    param o_file: output filename
    pre: construct_tree must be defined
    pre: BinaryTree must be defined
    post: o_file has a single string of letters
    complexity: O(N), where N = number of characters in i_file
    '''
    tree = construct_tree()

    f = open(i_file, 'r')
    i_str = f.read()
    f.close()

    o_str = ''

    i = 0

    while i < len(i_str):
        bin_str = ''
        while (i < len(i_str) - 1 and i_str[i] + i_str[i+1] != '0b'):
            bin_str += i_str[i]
            i += 1
        if i == len(i_str)-1:
            bin_str += i_str[i]
        
        if bin_str != '':
            o_str += str(tree.get(bin_str))

        i += 2

    f = open(o_file, 'w')   
    f.write(o_str)
    f.close()

"""
@author Gabriela Melo
@since 21/05/2015
@modified 22/05/2015
"""

from task2 import *
from task1 import *
from task3 import *

def dec_morse_tree():
    tree = BinaryTree()

    string = ''

    tree.add('a', '10111')
    tree.add('b', '111010101')
    tree.add('c', '11101011101')
    tree.add('c', '11101011101')
    tree.add('d', '1110101')
    tree.add('e', '1')
    tree.add('f', '101011101')
    tree.add('g', '111011101')
    tree.add('h', '1010101')
    tree.add('i', '101')
    tree.add('j', '1011101110111')
    tree.add('k', '111010111')
    tree.add('l', '101110101')
    tree.add('m', '1110111')
    tree.add('n', '11101')
    tree.add('o', '11101110111')
    tree.add('p', '10111011101')
    tree.add('q', '1110111010111')
    tree.add('r', '1011101')
    tree.add('s', '10101')
    tree.add('t', '111')
    tree.add('u', '1010111')
    tree.add('v', '101010111')
    tree.add('w', '101110111')
    tree.add('x', '11101010111')
    tree.add('y', '1110101110111')
    tree.add('z', '11101110101')

    return tree

def decode(i_str):
    tree = dec_morse_tree()
    o_str = ''
    i = 0

    while i < len(i_str):
        bin_str = ''
        while (i < len(i_str) - 2 and i_str[i] + i_str[i+1] + i_str[i+2] != '000'):
            bin_str += i_str[i]
            i += 1
        if i == len(i_str)-2:
            bin_str += i_str[i] + i_str[i+2]
        
        if bin_str != '':
            o_str += str(tree.get(bin_str))
        
        i += 3

    return o_str

def encode(i_str):
    o_str = ''
    for char in i_str:
        if char == 'a':
            o_str += '10111000'
        elif char == 'b':
            o_str += '111010101000'
        elif char == 'c':
            o_str += '11101011101000'
        elif char == 'd':
            o_str += '1110101000'
        elif char == 'e':
            o_str += '1000'
        elif char == 'f':
            o_str += '101011101000'
        elif char == 'g':
            o_str += '111011101000'
        elif char == 'h':
            o_str += '1010101000'
        elif char == 'i':
            o_str += '101000'
        elif char == 'j':
            o_str += '1011101110111000'
        elif char == 'k':
            o_str += '111010111000'
        elif char == 'l':
            o_str += '101110101000'
        elif char == 'm':
            o_str += '1110111000'
        elif char == 'n':
            o_str += '11101000'
        elif char == 'o':
            o_str += '11101110111000'
        elif char == 'p':
            o_str += '10111011101000'
        elif char == 'q':
            o_str += '1110111010111000'
        elif char == 'r':
            o_str += '1011101000'
        elif char == 's':
            o_str += '10101000'
        elif char == 't':
            o_str += '111000'
        elif char == 'u':
            o_str += '1010111000'
        elif char == 'v':
            o_str += '101010111000'
        elif char == 'w':
            o_str += '101110111000'
        elif char == 'x':
            o_str += '11101010111000'
        elif char == 'y':
            o_str += '1110101110111000'
        elif char == 'z':
            o_str += '11101110101000'

    return o_str

string = encode('abcdefghijklmnopqrstuvwxyz')
print(decode(string))

def compare_morse_ascii(i_file):
    for i in range(len(i_file)):
        f = open(i_file[i], 'r')
        string = f.read()
        f.close()

        write_letters(i_file[i], i_file[i])

        morse = encode(string)
        write_ascii(i_file[i], 'empty.txt')
        f = open('empty.txt', 'r')
        ascii = f.read()
        f.close()
        
        if len(ascii) < len(morse):
            print('ascii is shorter for file ' + i_file[i])
        elif len(ascii) > len(morse):
            print('morse is shorter for file ' + i_file[i])
        else:
            print('same length for file ' + i_file[i])

i_file = []
i_file.append('test.txt')
i_file.append('TheGreatGatsby.txt')
compare_morse_ascii(i_file)