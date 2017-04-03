"""
@author Gabriela Melo
@since 23/04/2015
@modified 01/05/2015
"""
class Stack:
	def __init__(self, size):
		assert size > 0, "Size should be positive"

		self.the_array = size*[None]
		self.count = 0
		self.top = -1

	def is_empty(self):
		return self.__len__() == 0

	def is_full(self):
		return self.__len__() >= len(self.the_array)

	def reset(self):
		self.count = 0
		self.top = -1

	def pop(self):
		assert not self.is_empty(), "Stack is empty"

		item = self.the_array[self.top]
		self.top -= 1
		self.count -= 1

		return item

	def push(self, item):
		assert not self.is_full(), "Stack is full"

		self.top += 1
		self.the_array[self.top] = item
		self.count += 1

	def peek(self):
		assert not self.is_empty(), "Stack is empty"

		return self.the_array[self.top]

	"""
	@param the stack itself
	@pre none
	@post returns amount of items in stack
	@complexity best = worse = O(1)
	"""
	def __len__(self):
		return self.count

	"""
	@param the stack itself
	@pre none
	@post string with items in stack separated 
		by spaces and starting from the one at the top
	@complexity best = worse = O(N)
	"""
	def __str__(self):
		a_string = ""
		for n in range(self.count -1, -1 , -1):
			a_string += str(self.the_array[n])
			if n != 0:
				a_string += " "
		return a_string

"""
@param none
@pre class Stack and __len__ are defined
@post returns True if __len__ is working properly, 
			False if not
@complexity best = worse = O(1)
"""
def test_len():
	correct = True
	my_stack = Stack(3)
	my_stack.push(2)
	if my_stack.__len__() != 1:
		correct = False
	my_stack.push('x')
	if my_stack.__len__() != 2:
		correct = False
	my_stack.push('!')
	if my_stack.__len__() != 3:
		correct = False
	return correct

"""
@param none
@pre class Stack and __str__ are defined
@post returns True if __str__ is working properly, 
			False if not
@complexity best = worse = O(1)
"""
def test_str():
	correct = True
	my_stack = Stack(3)
	my_stack.push(2)
	if my_stack.__str__() != '2':
		correct = False
	my_stack.push('x')
	if my_stack.__str__() != 'x 2':
		correct = False
	my_stack.push('!')
	if my_stack.__str__() != '! x 2':
		correct = False
	return correct
