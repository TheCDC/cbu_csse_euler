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
		"""Create a deep copy using the serial of the table"""
		return SudokuTable(self.serial())


	def serial(self):
		"""Converts the SudokuTable object to a serial that can be used to recreate the table. Implicity contains
		size information"""
		serial = ''
		for row in self.table:
			for item in row:
				serial += chr(item + ord('0'))

		return serial


	def get(self, x, y):
		return self.table[y][x]


	def set(self, x, y, value):
		self.table[y][x] = value


	def row(self, y):
		return self.table[y]


	def col(self, x):
		return [self.table[i][x] for i in range(self.size)]


	def subgrid(self, n):
		"""Returns the nth subgrid of the table, with 0 being the top left subgrid"""
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
		"""Returns a list of all the allowed values for the element in x, y"""
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
		"""Returns true if all values of the table are filled"""
		for row in self.table:
			for item in row:
				if item == 0:
					return False
		return True


	def breaksRules(self, subset):
		"""Checks if a subset of the table (row, column, or subgrid) breaks any Sudoku rules"""
		expected = [i for i in range(1, self.size + 1)]
		for item in subset:
			if item:
				try:
					expected.remove(item)
				except ValueError:
					return True
		return False


	def anyBreaksRules(self):
		"""Checks for any rule breaking in the entire table"""
		for n in range(self.size):
			if self.breaksRules(self.row(n)) or self.breaksRules(self.col(n)) or self.breaksRules(self.subgrid(n)):
				return True
		return False


	def isSolved(self):
		"""Returns true if the table is fully solved"""
		return self.isComplete() and not self.anyBreaksRules()


	def findFreebies(self):
		"""Finds any freebies in the table, returning the number of freebies found"""
		found = 0
		for y in range(self.size):
			for x in range(self.size):
				choices = self.possibles(x, y)
				if len(choices) == 1:
					self.set(x, y, choices.pop())
					found += 1

		return found


	def findAllFreebies(self):
		"""Finds all possible freebies in the table, including those cascaded from earlier freebies"""
		while(self.findFreebies()):
			1

	def firstUnknown(self):
		"""Returns the coordinates of the first 0 in the SudokuTable as an array"""
		for y in range(self.size):
			for x in range(self.size):
				if self.get(x, y) == 0:
					return [x, y]

		return False


	def solve(self):
		"""Solves the table using freebies and recursive backtracking"""
		self = SudokuTable.guessSolve(self)


	def guessSolve(board, depth = 0):
		"""Returns a solved version of the table without solving the original"""
		#print(depth)

		# Find available freebies. May slow down or speed up the function, depending on the table.
		board.findAllFreebies()
		if(board.isSolved()):
			return board

		# Guess, recurse, and backtrack
		target = board.firstUnknown()
		for possible in board.possibles(target[0], target[1]):
			board.set(target[0], target[1], possible)
			if board.isSolved():
				return board
			nextStep = SudokuTable.guessSolve(board.copy(), depth + 1)
			if nextStep != -1:
				return nextStep
			board.set(target[0], target[1], 0)

		return -1


	def print(self):
		for row in self.table:
			print(str(row))