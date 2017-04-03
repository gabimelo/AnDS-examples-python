def quickSort(l, low, high, count):
	if low < high:
		index = partition(l, low, high)
		count = quickSort(l, low, index-1, count)
		count = quickSort(l, index+1, high, count)
	return count+1

def partition(l, low, high):
	from random import randint 
	index = randint(low, high)
	pivot = l[index]
	swap(l, index, high)
	i = low-1
	j = low
	while j < high:
		if l[j] < pivot:
			i+=1
			swap(l, i, j)
		j += 1
	swap(l, high, i+1)
	return i+1

def swap(a_list, pos1, pos2):
    temp = a_list[pos1]
    a_list[pos1] = a_list[pos2]
    a_list[pos2] = temp

# from random import randint 
# l = []
# for i in range(30):
# 	num = randint(0,500)
# 	l.append(num)
# print(quickSort(l, 0, len(l)-1, 0))
# print(l)

def binarySearch(k, l, low, high):
	if high < low:
		return -1
	mid = (low+high)//2
	if l[mid] > k:
		return binarySearch(k, l, low, mid-1)
	elif l[mid] < k:
		return binarySearch(k, l, mid+1, high)
	else:
		return mid

# print(binarySearch(3, [1, 2, 2, 3, 2, 2], 0, 5))

def counting_sort(A, k, d):
	B = len(A)*[0]
	v = k * [0]
	for j in range(len(A)):
		num = A[j]%10**(d+1)//10**d
		v[num] += 1
# v[i]: the number of elements equal to i
	for i in range(1,k):
		v[i] += v[i-1]
# v[i]: the number of elements <= i
	for j in reversed(range(len(A))):
		num = A[j]%10**(d+1)//10**d
		v[num] -= 1
		B[v[num]] = A[j]
	return B

# A = [1, 0, 0, 1, 3, 2]
# print(counting_sort(A, 4, 0))

def radix_sort(A, d):
	for i in range(d):
		A = counting_sort(A, 9, i)
	return A

# A = [126, 328, 636, 341, 416, 131, 328]
# print(radix_sort(A, 3))

def choose(n,k):
	if n == k or k == 0:
		return 1
	else:
		return choose(n-1,k-1) + choose(n-1,k)

def mem_choose(n,k):
	assert k <= n
	T = []
	for i in range(n+1):
		t = []
		for j in range(k+1):
			t.append(0)
		T.append(t)
	T = mem_choose2(n, k, T)
	return T[n][k]

def mem_choose2(n, k, T):
	if n == k or k == 0:
		T[n][k] = 1
	else:
		if T[n-1][k-1] == 0:
			T = mem_choose2(n-1, k-1, T)
		if T[n-1][k] == 0:
			T = mem_choose2(n-1, k, T)
		T[n][k] = T[n-1][k-1] + T[n-1][k]
	return T

# print(choose(25,7))
# print(mem_choose(25,7))