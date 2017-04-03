'''
task1.

edit distance
but each cell keeps track of max
max starts at zero
whenever you move diagonally with an increase of 0 in cost, 
	-> max of the new cell is max of previous+1
when moving horizontally or vertically, doesn't change value
the movement is chosen from the one that gives max value

'''
def longestCommonSubseq(A, B):
	m = len(A)
	n = len(B)
	# create table T of size mXn, initialized to 0
	T = []
	for _ in range(m+1):
		T.append([0 for _ in range(n+1)])

	for i in range(1,m+1):
		for j in range(1,n+1):
			if A[i-1:i] == B[j-1:j]:
				temp = T[i-1][j-1]+1 
			else:
				temp = T[i-1][j-1]
			T[i][j] = max(temp, T[i-1][j], T[i][j-1])	
	return T[m][n]

print(longestCommonSubseq('abcde', 'xyabcz'))

'''
task2.

binary search
'''

def maxInShiftedA(a, low, high):
	# returns index of max
	mid = (low+high)//2
	if mid == low:
		if a[mid] > a[high]:
			return mid
		else:
			return high
	if a[mid] >= a[low]:
		return maxInShiftedA(a, mid+1, high)
	else:
		return maxInShiftedA(a, low, mid-1)

a = [35,42,5,15,27,29]
print(a[maxInShiftedA(a, 0, len(a)-1)])

''' 
task 3.

basic idea: if you can get to the second next, don't 
stop at next 

proof on paper

run-time complexity: O(n)
'''
def gasStops(m, d):
	result = []
	cap = m
	n = len(d)
	for i in range(n-1):
		if d[i+1] > cap:
			cap = d[i] + m
			result.append(d[i])
	return result

print(gasStops(10,[6,8,12,17,23]))

'''
task 4.

there will need to be a queen on each row
stack holds where each queen is positioned
	first item in stack indicates index of queen on first row 
	second item in stack indicates index of queen on second row
	....
if gets to an invalid configuration, pop last queen from stack and keep on trying from there
'''
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

    def __len__(self):
        return self.count

    def __str__(self):
        a_string = ""
        for n in range(self.count -1, -1 , -1):
            a_string += str(self.the_array[n])
            if n != 0:
                a_string += " "
        return a_string

def nQueens(N):
	S = Stack(N)
	pos = 0
	while not S.is_full():
		while pos < N and not checkValidity(S, pos):
			pos += 1
		if pos != N:
			S.push(pos)
			pos = 0
		while pos == N:
			pos = S.pop() + 1
	printSolution(S)

def checkValidity(S, pos):
	a = []
	while not S.is_empty():
		a.append(S.pop())
	a.reverse()
	for item in a:
		S.push(item)
	for i in range(len(a)):
		if a[i] == pos or a[i]+len(a)-i == pos or a[i]-len(a)+i == pos:			
			return False	
	return True

def printSolution(S):
	result = []
	N = len(S)
	while not S.is_empty():
		pos = S.pop()
		tmp = []
		for i in range(N):
			if i == pos:
				tmp.append("Q")
			else:
				tmp.append("*")
		result.append(tmp)
	# result.reverse()
	for item in result:
		print(item)

nQueens(9)