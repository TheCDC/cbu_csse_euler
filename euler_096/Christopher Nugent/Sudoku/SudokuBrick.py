class SudokuBrick:

	def __init__(self):
		self.value = 0
		self.possible = {1, 2, 3, 4, 5, 6, 7, 8 , 9}