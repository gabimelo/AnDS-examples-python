def fac(n):
	if n == 1:
		return 1
	else:
		return n*fac(n-1)

def it_fac(n):
	fact = 1
	for i in range(2,n+1):
		fact = fact*i
	return fact

def Fibonnaci(n):
	if n in (0,1):
		return 1
	return fib(n, 1, [1,1])

def fib(max, j, a):
	if j == max:
		return a[j]
	else:
		a.append(a[j-1]+a[j])
		return fib(max, j+1, a)

# print(Fibonnaci(1))

def multMatrices(A, B):
	aRows = len(A)
	bRows = len(B)
	bCols = len(B[0])

	result = []
	for i in range(aRows):
		tmp = []
		for j in range(bCols):
			temp = 0
			for k in range(bRows):
				temp += A[i][k]*B[k][j]
			tmp.append(temp)
		result.append(tmp)
	return result

print(multMatrices([[1,3,5,7],[2,4,6,8]],[[1,8,9],[2,7,10],[3,6,11],[4,5,12]]))