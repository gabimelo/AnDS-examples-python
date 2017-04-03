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

def read_array(fname):
	f = open(fname, 'r')
	string = f.read()
	f.close()
	A = [int(x) for x in string.split('	')]
	return A

class AVLNode():
	def __init__(self, key, left, right):
		self.key = key	
		self.left = left
		self.right = right
		self.height = 0

class AVLTree():
	def __init__(self):
		self.root = None

	def insert(self, x):
		self.root = self.insert_aux(x, self.root)

	def insert_aux(self, x, current):
		if current is None:
			return AVLNode(x, None, None)
		if x < current.key:
			current.left = self.insert_aux(x, current.left)
		elif x > current.key:
			current.right = self.insert_aux(x, current.right)
		# do nothing if duplicate key
		return self.balance(current)

	def balance(self, current):
		if self.height(current.left) - self.height(current.right) > 1:
			if self.height(current.left.left) > self.height(current.left.right):
				current = self.rRotate(current)
			else:
				current = self.lrRotate(current)
		elif self.height(current.right) - self.height(current.left) > 1:
			if self.height(current.right.right) > self.height(current.right.left):
				current = self.lRotate(current)
			else:
				current = self.rlRotate(current)
		current.height = 1 + max(self.height(current.right), self.height(current.left))
		return current

	def lRotate(self,current):
		tmp = current.right
		current.right = tmp.left
		tmp.left = current
		current.height = 1 + max(self.height(current.right), self.height(current.left))
		return tmp

	def rRotate(self,current):
		tmp = current.left
		current.left = tmp.right
		tmp.right = current
		current.height = 1 + max(self.height(current.right), self.height(current.left))
		return tmp	

	def lrRotate(self,current):
		current.left = self.lRotate(current.left)
		current = self.rRotate(current)
		return current

	def rlRotate(self,current):
		current.right = self.rRotate(current.right)
		current = self.lRotate(current)
		return current

	def height(self, current):
		if current is None:
			return -1
		return current.height

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

def task5():
	A = read_array('numbers.txt')
	# A = [100,20,12,2]
	tree = insert_array(A, "avl")
	print("Inorder traversal of tree read from file:")
	print(str(tree))
	print("\nPaths to all items in tree read from file:")
	tree.search_print(4, tree.root)
	# for item in A:
	tree.search_print(6, tree.root)

def heapify(array, n):
	array[0] = n
	i = array[0]//2
	while i > 0:
		percolateDown(array, i)
		i -= 1
	return array

def percolateDown(array, i):
	while i*2 <= array[0]:
		child = get_largest_child(array, i)
		if array[child] < array[i]:
			break
		swap(array, child, i)
		i = child

def get_largest_child(array, i):
	try:
		assert (i*2+1)<=array[0]
	except AssertionError:
		return i*2
	if array[i*2] > array[i*2+1]:
		return i*2
	else:
		return i*2+1

def swap(array, pos1, pos2):
    temp = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = temp

def delete_max(array, n):
	swap(array, 1, n)
	array[0] -= 1
	percolateDown(array, 1)

def heap_sort(array, print_flag):
	array = heapify(array, len(array)-1)
	while array[0] > 0:
		if print_flag:
			print(str(array))
		delete_max(array,array[0])

def task6():
	print("\n-------------------\n      Task 6\n-------------------")
	array = read_array('numbers.txt')
	array = [0] + array
	heap_sort(array, True)
	print("\n")

if __name__ == '__main__':
	task5()
	task6()