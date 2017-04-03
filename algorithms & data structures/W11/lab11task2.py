def read_file(fname):
    f = open(fname, 'r')
    lines = [int(line.rstrip('\n')) for line in f]
    f.close()
    return lines

INF = 9999999999999

def orderMatrix(c):
	m = []
	lastChange = []
	n = len(c)

	for left in range(1,n):
		m.append([0 for _ in range(n-1)])
		lastChange.append([None for _ in range(n-1)])

	for L in range(2, n):
		for i in range(n-L):
			j = i + L - 1
			m[i][j] = INF
			for k in range(i, j):
				q = m[i][k]+m[k+1][j]+c[i]*c[k+1]*c[j+1]
				if q < m[i][j]:
					 m[i][j] = q
					 lastChange[i][j] = k+1
	return m, lastChange

print(orderMatrix(read_file("dimensions.txt")))