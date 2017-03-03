class SudokuTable:
	

	def __init__(self, para):
		if type(para) == type(1):
			self.table = [[0 for column in range(para**2)] for row in range(para**2)]
			self.root = para
			self.size = para**2
		elif type(para) == type("abc"):
			total = len(para)
			if(total**(1/4) % 1 != 0):
				raise ValueError
			self.size = int(total**(1/2)) 
			self.root = int(total **(1/4))
			self.table = [[0 for column in range(self.root**2)] for row in range(self.root**2)]
			for i in range(total):
				#print(i)
				#print(i // self.size)
				#print(i % self.size)
				self.table[i // self.size][i % self.size] = ord(para[i]) - ord('0')		

	def copy(self):
		return SudokuTable(self.serial())


	def get(self, x, y):
		return self.table[y][x]


	def set(self, x, y, value):
		self.table[y][x] = value


	def row(self, y):
		return self.table[y]


	def col(self, x):
		return [self.table[i][x] for i in range(self.size)]


	def subgrid(self, n):
		y = self.root * (n // self.root)
		x = self.root * (n % self.root)
		#print("Trying grid of " + str(x) + ", " + str(y) )
		return self.subgridOf(x, y)


	def subgridOf(self, x, y):
		"""Returns a list of the elements in the same subgrid as the element in (x, y)"""
		elements = []
		firstRow = self.root * (y // self.root)
		firstCol = self.root * (x // self.root)
		
		for row in range(firstRow, firstRow + self.root):
			#print("Accessing through (" + row + ',' + (firstCol + self.root - 1) + ")")
			elements.extend([self.table[row][col] for col in range(firstCol, firstCol + self.root)])

		return elements


	def possibles(self, x, y):
		if self.get(x, y) != 0:
			return []

		possibles = [i for i in range(1, self.size + 1)]
		for other in self.col(x):
			#no errors should be raised here
			if other:
				possibles.remove(other)
		for other in self.row(y):
			try:
				if other:
					possibles.remove(other)
			except ValueError:
				1
		for other in self.subgridOf(x, y):
			try:
				if other:
					possibles.remove(other)
			except ValueError:
				1
		return possibles


	def isComplete(self):
		for row in self.table:
			for item in row:
				if item == 0:
					return False
		return True


	def breaksRules(self, subset):
		expected = [i for i in range(1, self.size + 1)]
		for item in subset:
			if item:
				try:
					expected.remove(item)
				except ValueError:
					return True
		return False


	def anyBreaksRules(self):
		for n in range(self.size):
			if self.breaksRules(self.row(n)) or self.breaksRules(self.col(n)) or self.breaksRules(self.subgrid(n)):
				return True
		return False


	def isSolved(self):
		return self.isComplete() and not self.anyBreaksRules()


	def isSolved(board):
		return board.isSolved()


	def findFreebies(self):
		found = 0
		for y in range(self.size):
			for x in range(self.size):
				choices = self.possibles(x, y)
				if len(choices) == 1:
					self.set(x, y, choices.pop())
					found += 1

		return found


	def findAllFreebies(self):
		while(self.findFreebies()):
			1


	def guessSolve(self):
		#find available freebies
		self.findAllFreebies()

		if self.isSolved():
			return self

		for




	def print(self):
		for row in self.table:
			print(str(row))

	def serial(self):
		serial = ''
		for row in self.table:
			for item in row:
				serial += chr(item + ord('0'))

		return serial