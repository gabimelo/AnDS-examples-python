"""
@author Gabriela Melo
@since 05/05/2015
@modified 05/05/2015
"""
class Node:
	def __init__(self, item = None, link = None):
		self.item = item
		self.next = link

	def __str__(self):
		return(str(self.item))

	def print_structure(node):
		while node is not None:
			print(node, end = "")
			node = node.next
		print()
