'''
@ author: Brian Ezra, Gabriela Melo
@ since: 21/05/2015
'''

from task1 import *
from task2 import *
from task3 import *

def test_qty_chars():
	correct = True

	f = open('test.txt', 'w')
	f.write('test test test')
	f.close()

	if qty_chars('test.txt') != 14:
		correct = False

	try:
		qty_chars('test')
		correct = False
	except:
		pass

	return correct

def test_write_letters():
	correct = True

	f = open('test.txt', 'w')
	f.write('test TEST test')
	f.close()

	write_letters('test.txt', 'empty.txt')

	f = open('empty.txt', 'r')
	string = f.read()
	f.close()

	if string != 'testtesttest':
		correct = False

	try:
		write_letters('test.tx', 'empty')
		correct = False
	except:
		pass

	return correct

def test_letter_freq():
	correct = True
	
	f = open('test.txt', 'w')
	f.write('testtset')
	f.close()

	string = letter_freq('test.txt')
	if string != 't 4 e 2 s 2 a 0 b 0 c 0 d 0 f 0 g 0 h 0 i 0 j 0 k 0 l 0 m 0 n 0 o 0 p 0 q 0 r 0 u 0 v 0 w 0 x 0 y 0 z 0 ':
		correct = False

	f = open('test.txt', 'w')
	f.write('test tset')
	f.close()

	string = letter_freq('test.txt')
	if string != 't 4 e 2 s 2 a 0 b 0 c 0 d 0 f 0 g 0 h 0 i 0 j 0 k 0 l 0 m 0 n 0 o 0 p 0 q 0 r 0 u 0 v 0 w 0 x 0 y 0 z 0 ':
		correct = False

	try:
		letter_freq('test.tx')
		correct = False
	except:
		pass

	return correct

def test_BinaryTree():
	tree = BinaryTree()
	tree.add(4, '')
	tree.add(2, '0')
	tree.add(1, '00')
	tree.add(3, '01')
	tree.add(6, '1')
	tree.add(5, '10')
	tree.add(7, '11')
	correct = True

	if tree.get('') != 4:
		correct = False
	if tree.get('0') != 2:
		correct = False
	if tree.get('00') != 1:
		correct = False
	if tree.get('01') != 3:
		correct = False
	if tree.get('1') != 6:
		correct = False
	if tree.get('10') != 5:
		correct = False
	if tree.get('11') != 7:
		correct = False
	if tree.inorder_str() != '1234567':
		correct = False
	try:
		tree.get('00000')
		correct = False
	except AssertionError:
		pass

	return correct

def test_write_ascii():
	correct = True

	f = open('test.txt', 'w')
	f.write('test TEST test')
	f.close()

	write_ascii('test.txt', 'empty.txt')

	f = open('empty.txt', 'r')
	string = f.read()
	f.close()

	expected_str = ''
	for _ in range(3):
		expected_str += str(bin(ord('t')))
		expected_str += str(bin(ord('e')))
		expected_str += str(bin(ord('s')))
		expected_str += str(bin(ord('t')))
	if string != expected_str:
		correct = False

	try:
		write_ascii('test.tt', 'empty')
		correct = False
	except:
		pass

	return correct

def test_construct_tree():
	my_str = ''
	tree = construct_tree()
	string = tree.inorder_str()
	i = 0
	while i < len(string):
		try:
			while string[i] == 'N':
				i += 4
			my_str += string[i]
			i += 1
		except IndexError:
			pass

	correct = True
	if my_str != 'abcdefghijklmnopqrstuvwxyz':
		correct = False
	return correct

def test_write_chars():
	correct = True

	string = ''
	string += str(bin(ord('t'))) + str(bin(ord('e')))
	string += str(bin(ord('s'))) + str(bin(ord('t')))
	
	f = open('test.txt', 'w')
	f.write(string)
	f.close()

	write_chars('test.txt', 'empty.txt')

	f = open('empty.txt', 'r')
	string = f.read()
	f.close()

	if string != 'test':
		correct = False

	try:
		write_chars('test.tt', 'empty')
		correct = False
	except:
		pass

	return correct

if not test_qty_chars():
	print('qty_chars not working')
elif not test_write_letters():
	print('write_letters not working')
elif not test_letter_freq():
	print('letter_freq not working')
elif not test_BinaryTree():
	print('BinaryTree not working!')
elif not test_write_ascii():
	print('write_ascii not working!')
elif not test_construct_tree():
	print('construct_tree not working')
elif not test_write_chars():
	print('write_chars not working')
else:
	print('All functions are working properly!')