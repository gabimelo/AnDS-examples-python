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