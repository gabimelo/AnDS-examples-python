class Prime:
	def __init__(self, max):
		self.max = max

	def __iter__(self):
		return PrimeIterator(self.max)

class PrimeIterator:
	def __init__(self, max):
		self.current = 2
		self.max = max

	def __iter__(self):
		return self

	def __next__(self):
		prime = False
		while (not prime and self.current < self.max):
			aux = 2
			prime = True
			while aux < self.current:
				if self.current % aux == 0:
					prime = False
				aux += 1
			self.current += 1
		if self.current == self.max:
			raise StopIteration
		return (self.current - 1)

num = Prime(20)

for i in num:
	print(i)
