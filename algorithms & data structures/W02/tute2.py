def ones_in_bin(n):
	if n < 2:
		return n
	return n%2+ones_in_bin(n//2)

def permute(str):
	permute2(str, 0, len(str)-1)

def permute2(str, low, high):
	if low == high:
		print(str)
	else:
		pos = low
		while pos < len(str):
			str = swap(str, pos, low)
			permute2(str, low+1, high)
			pos += 1

def swap(str, pos, low):
	str = str[:low] + str[pos:pos+1]+str[low:pos]+str[pos+1:]
	return str

permute('abc') 