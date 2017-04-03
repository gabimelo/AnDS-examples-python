# Rabin-Karp
def rabin_karp(P,T):
	x = 10
	q = 7
	m,n= len(P), len(T)
	p,t,h = P[0], T[0], 1
	for i in range(1,m):
		p = (p * x + P[i]) % q
		t = (t * x + T[i]) % q
		h = (h * x) % q
	for s in range(n-m+1):
		if p == t:
			if P == T[s:s+m]:
				print('Pattern occurs with shift ' + str(s))
		if s<n-m:
			t = ((t - h*T[s])*x + T[s+m])%q
# rabin_karp([1,2,3], [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,1,2,3])

# Boyer-Moore
def boyer_moore(P,T):
	m,n= len(P), len(T)
	L = [-1]*10
	for i in range(m):
		L[P[i]] = m-i-1
	j = m - 1
	while j < n:
		c = 0
		while c < m and P[m-c-1] == T[j-c]:
			c += 1
		if c == m:
			print('Pattern occurs with shift ' + str(j-(m-1)))
		pos = L[T[j-c]]
		if pos > c:
			j = j - c + pos
		else:
			j = j + m
# boyer_moore([1,2,3], [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,1,2,3])

# task 2
'''
@ author: Brian Ezra, Gabriela Melo
@ since: 15/05/2015
@ modified: 22/05/2015
'''

class TreeNode:
    def __init__(self, item):
        self.item = item
        self.children = []

class BinaryTree:
    def __init__(self):
        self.root = TreeNode(None)

    def insertWord(self, word):	
        self.add_aux(self.root, word)

    def add_aux(self, current, item):
        if len(item) == 0:
        	return
        if len(current.children) == 0:
        	current.children.append([item[:1], TreeNode(item[:1])])
        	self.add_aux(current.children[0][1], item[1:])
        	return
        for i in range(len(current.children)):
        	if item[:1] == current.children[i][0]:
        		self.add_aux(current.children[i][1], item[1:])
        		return
        	if item[:1] < current.children[i][0]:
        		current.children.insert(i, [item[:1], TreeNode(item[:1])])		
        		self.add_aux(current.children[i][1], item[1:])
        		return
        i+=1
        current.children.insert(i, [item[:1], TreeNode(item[:1])])		
        self.add_aux(current.children[i][1], item[1:])
        return

    def searchWord(self, word):
    	return self.searchWord_aux(word, self.root)

    def searchWord_aux(self, word, current):
    	if len(word) == 0:
        	return True
    	for i in range(len(current.children)):
        	if word[:1] == current.children[i][0]:
        		return self.searchWord_aux(word[1:], current.children[i][1])
    	return False

    def deleteWord(self, word):
    	for i in range(len(word),0, -1):
    		self.deleteWord_aux(self.root, word[:i])

    def deleteWord_aux(self, current, word):
    	if len(word) == 1:
    		# print(current.item)
    		# print(word)
    		for i in range(len(current.children)):
    			if word == current.children[i][0]:
    				if len(current.children[i][1].children) == 0:
    					current.children.pop(i)
    				return
    	for i in range(len(current.children)):
        	if word[:1] == current.children[i][0]:
        		self.deleteWord_aux(current.children[i][1], word[1:])
        		return

    def printWords(self):
    	word = ""
    	self.printWords_aux(self.root, word)

    def printWords_aux(self, current, word):
    	if len(current.children) == 0:
    		print(word)
    	for i in range(len(current.children)):
    		self.printWords_aux(current.children[i][1], word+current.children[i][0])
    
tree = BinaryTree()
tree.insertWord("rubicundus")
tree.insertWord("romulus")
tree.insertWord("romane")
tree.insertWord("rubicon")
tree.insertWord("ruber")
tree.insertWord("romanus")
tree.insertWord("rubens")
print(tree.searchWord("rubicundus"))
print(tree.searchWord("rubens"))
print(tree.searchWord("rubicunds"))
tree.printWords()
tree.deleteWord("rubicundus")
# print(tree.root.children[0][1].children[1][1].children[0][1].children[1][1].children[0][1].children[0][0])
tree.deleteWord("rubens")
print(tree.searchWord("rubicundus"))
print(tree.searchWord("rubens"))
print(tree.searchWord("rubicunds"))
tree.printWords()

# task 3
def task3():
	def binarySearch(P, SA, text, low, high, i):
		if high < low:
			return -1,-1
		mid = (low+high)//2
		if text[SA[mid]:][i:i+1] > P:
			return binarySearch(P, SA, text, low, mid-1, i)
		elif text[SA[mid]:][i:i+1] < P:
			return binarySearch(P, SA, text, mid+1, high, i)
		else:
			mini = maxi = mid
			while mini>low and text[SA[mini-1]:][i:i+1] == text[SA[mini]:][i:i+1]:
				mini -= 1
			while maxi<high and text[SA[maxi+1]:][i:i+1] == text[SA[maxi]:][i:i+1]:
				maxi += 1
			return mini, maxi

	text = "mississippi"
	SA = [10,7,4,1,0,9,8,6,3,5,2]
	pattern = "nn"

	if len(pattern)>0:
		low = 0
		high = len(SA)-1
		found = True
		for i in range(len(pattern)):
			low, high = binarySearch(pattern[i:i+1], SA, text, low, high, i)
			if low == -1:
				found = False
				break
		if found:
			print(high-low+1)
		else:
			print(-1)
	else:
		print("empty pattern")

# task3()