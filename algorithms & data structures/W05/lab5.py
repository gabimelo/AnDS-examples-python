class maxHeap:
	def __init__(self):
		self.count = 0
		self.array = [None]

	def buildHeap(self, a):
		self.count = len(a)
		for item in a:
			self.array.append(item)
		i = self.count//2
		while i > 0:
			self.percolateDown(i)
			i -= 1

	def percolateDown(self, i):
		while i*2 <= self.count:
			child = self.get_largest_child(i)
			if self.array[child] < self.array[i]:
				break
			self.swap(child, i)
			i = child

	def get_largest_child(self, i):
		try:
			assert (i*2+1)<=self.count
		except AssertionError:
			return i*2
		if self.array[i*2] > self.array[i*2+1]:
			return i*2
		else:
			return i*2+1

	def swap(self, pos1, pos2):
	    temp = self.array[pos1]
	    self.array[pos1] = self.array[pos2]
	    self.array[pos2] = temp

	def __str__(self):
		return str(self.array)

heap = maxHeap()
heap.buildHeap([8,9,2,3,7,5])
print(str(heap))

class TreeNode():
	def __init__(self, key, left, right):
		self.key = key	
		self.left = left
		self.right = right

class BinaryTree():
	def __init__(self):
		self.root = None

	def insert(self, x):
		if self.root is None:
			self.root = TreeNode(x, None, None)
		else:
			self.insert_aux(x, self.root)

	def insert_aux(self, x, current):
		if x < current.key:
			if current.left is None:
				current.left = TreeNode(x, None, None)
			else:
				self.insert_aux(x, current.left)
		else:
			if current.right is None:
				current.right = TreeNode(x, None, None)
			else:
				self.insert_aux(x, current.right)

	def __str__(self):
		# inorder taversal
		return self.inorder(self.root, '')

	def inorder(self, current, string):
		if current is not None:
			string = self.inorder(current.left, string)
			string += str(current.key) + " "
			string = self.inorder(current.right, string)
		return string

	def search_print(self, k, T):
		if T is None:
			print("the input number was not found in the BST")
		else:
			print(self.search_print_aux(k, T, ""))

	def search_print_aux(self, k, current, string):
		if current is None:
			string = "the input number was not found in the BST"
		else:
			if string != "":
				string += " -> "
			string += str(current.key)
			if current.key < k:
				string = self.search_print_aux(k, current.right, string)
			elif current.key > k:
				string = self.search_print_aux(k, current.left, string)
		return string
	
	def height(self):
		return self.height_aux(self.root)

	def height_aux(self, current):
		if current is None:
			return -1
		hl = self.height_aux(current.left)
		hr = self.height_aux(current.right)
		return 1 + max(hl,hr)

def insert_array(A, type):
	if type == "bin":
		tree = BinaryTree()
	elif type == "rb":
		tree = RBTree()
	elif type == "avl":
		tree = AVLTree()
	for i in A:
		tree.insert(i)
	return tree

def balanceCheck(tree):
	if tree.root is None:
		print("Tree is empty")
	else:
		if balanceCheck_aux(tree, tree.root) != "break":
			print("Tree is balanced")
		else:
			print("Tree is not balanced")

def balanceCheck_aux(tree, current):
	if current is None:
		return -1
	hl = balanceCheck_aux(tree, current.left)
	hr = balanceCheck_aux(tree, current.right)
	if hr == "break" or hl == "break" or hl - hr > 1 or hr - hl > 1:
		return "break"
	return 1 + max(hl,hr)

def leftistCheck(tree):
	if tree.root is None:
		print("Tree is empty")
	else:
		if leftistCheck_aux(tree, tree.root) != "break":
			print("Tree is leftist heap")
		else:
			print("Tree is not leftist heap")

def leftistCheck_aux(tree, current):
	if current is None:
		return -1
	distl = leftistCheck_aux(tree, current.left)
	distr = leftistCheck_aux(tree, current.right)
	if distr == "break" or distl == "break" or distr > distl:
		return "break"
	return 1 + min(distl,distr)

# tree = insert_array([3,2,4,1], "bin")
# print(str(tree))
# balanceCheck(tree)
# leftistCheck(tree)

class RBNode():
	def __init__(self, key, left, right, color):
		self.key = key	
		self.left = left
		self.right = right
		self.color = color # can be either "red" or "black"

class RBTree:
	def __init__(self):
		self.root = None

	def insert(self, x):
		self.root = self.insert_aux(x, self.root)
		if self.root.color == "red":
			self.root.color = "black"

	def insert_aux(self, x, current):
		if current is None:
			return RBNode(x, None, None, "red")
		if x < current.key:
			current.left = self.insert_aux(x, current.left)
		elif x > current.key:
			current.right = self.insert_aux(x, current.right)
		# do nothing if duplicate key
		return self.doubleRed(current)

	def doubleRed(self, current):
		if self.color(current.left) == "red" and self.color(current.right) == "red":
			if self.color(current.left.left) == "red" or self.color(current.left.right) == "red" or self.color(current.right.left) or self.color(current.right.right):
				current.color = "red"
				current.left.color = current.right.color = "black"
		elif self.color(current.left) == "red" and self.color(current.right) in ("black",-1):
			if self.color(current.left.left) == "red":
				current.color = "red"
				current = self.rRotate(current)
				current.color = "black"
			elif self.color(current.left.right) == "red":
				current.color = "red"
				current = self.lrRotate(current)
				current.color = "black"
		elif self.color(current.right) == "red" and self.color(current.left) in ("black",-1):
			if self.color(current.right.left) == "red":
				current.color = "red"
				current = self.rlRotate(current)
				current.color = "black"
			elif self.color(current.right.right) == "red":
				current.color = "red"
				current = self.lRotate(current)
				current.color = "black"
		return current

	def lRotate(self,current):
		tmp = current.right
		current.right = tmp.left
		tmp.left = current
		return tmp

	def rRotate(self,current):
		tmp = current.left
		current.left = tmp.right
		tmp.right = current
		return tmp	

	def lrRotate(self,current):
		current.left = self.lRotate(current.left)
		current = self.rRotate(current)
		return current

	def rlRotate(self,current):
		current.right = self.rRotate(current.right)
		current = self.lRotate(current)
		return current

	def color(self, current):
		if current is None:
			return -1
		return current.color

	def __str__(self):
		# inorder taversal
		return self.inorder(self.root, '')

	def inorder(self, current, string):
		if current is not None:
			string = self.inorder(current.left, string)
			string += str(current.key) + " "
			string = self.inorder(current.right, string)
		return string

	def search_print(self, k, T):
		if T is None:
			print("AVL Tree is empty")
		else:
			print(self.search_print_aux(k, T, ""))

	def search_print_aux(self, k, current, string):
		if current is not None:
			if string != "":
				string += " -> "
			string += str(current.key)
			if current.key < k:
				string = self.search_print_aux(k, current.right, string)
			elif current.key > k:
				string = self.search_print_aux(k, current.left, string)
		return string

A = [2,1,4,5,9,3,6,7]
tree = insert_array(A, "rb")
print("Inorder traversal of tree read from file:")
print(str(tree))
print("\nPaths to all items in tree read from file:")
for item in A:
	tree.search_print(item, tree.root)
print(tree.root.left.color)
print(tree.root.color)
# print(tree.root.right.left.left.color)
# print(tree.root.right.left.color)
# print(tree.root.right.color)
# print(tree.root.right.right.left.color)
# print(tree.root.right.right.color)
# print(tree.root.right.right.right.color)