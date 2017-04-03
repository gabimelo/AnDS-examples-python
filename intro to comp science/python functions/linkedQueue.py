"""
@author Gabriela Melo
@since 05/05/2015
@modified 05/05/2015
"""
class LinkedQueue:
	def __init__(self):
		self.rear = None
		self.front = None

	def is_empty(self):
		return self.front is None

	def is_full(self):
		return False

	def reset(self):
		self.rear = None
		self.front = None
	
	def append(self, item):
		import node
		node = node.Node(item, None)

		if self.is_empty():
			self.front = node
		else:
			self.rear.next = node

		self.rear = node

	def serve(self):
		assert not self.is_empty(), "Queue is empty"

		item = self.front.item
		self.front = self.front.next

		if self.is_empty():
			self.rear = None

		return item