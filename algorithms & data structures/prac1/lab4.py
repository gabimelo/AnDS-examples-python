def pow(m, n):
	if n == 0:
		return 1
	elif n == 1:
		return m
	else:
		from math import ceil
		return pow(m, n//2)*pow(m, ceil(n/2))

# print(pow(3,1000))

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

def insert_array(A):
	tree = BinaryTree()
	for i in A:
		tree.insert(i)
	return tree

def read_array(fname):
	f = open(fname, 'r')
	string = f.read()
	f.close()
	A = [int(x) for x in string.split('	')]
	return A

def permute_array(A):
	from random import randint
	for i in range(len(A)):
		j = randint(i,len(A)-1)
		swap(A, i, j)
	return A

def swap(A, pos1, pos2):
    temp = A[pos1]
    A[pos1] = A[pos2]
    A[pos2] = temp

def height_randomBST(N):
	A = [i for i in range(1, N+1)]
	A = permute_array(A)
	tree = insert_array(A)
	print(tree.height())

def main():
	A = read_array('numbers.txt')
	tree = insert_array(A)
	print("Inorder traversal of tree read from file:")
	print(str(tree))
	print("\nPaths to all items in tree read from file:")
	tree.search_print(7, tree.root)
	tree.search_print(10, tree.root)
	# tree.search_print(2, tree.root)
	# tree.search_print(100, tree.root)
	print("\nHeight of random tree:")
	height_randomBST(5)

if __name__ == '__main__':
	main()
