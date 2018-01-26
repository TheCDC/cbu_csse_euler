from Sudoku import SudokuTable

f = open("data.txt", 'r')

total = 0

for puzzle in range(50):
    problem = ''
    f.readline()
    for row in range(9):
        problem += f.readline()[:9]
        #print(problem)

    total += SudokuTable.guessSolve(SudokuTable(problem)).euler()

print(total)
