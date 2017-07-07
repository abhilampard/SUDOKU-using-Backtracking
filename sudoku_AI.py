from sudoku_solver import solver
from sudoku_create import sudoku,disp,easy_gen,hard_gen,swap,sudoku_input

grid=[[0 for i in range(9)] for j in range(9)]

c=input(" 1. For Easy Sudoku\n 2. For Hard Sudoku\n 3. For own input")

if(c==1):
	print "Generating easy mode"
	easy_gen()
elif(c==2):
	print "Generating hard mode"
	hard_gen()
elif(c==3):
	print "Enter Your own input(0 for blank box)"
	sudoku_input()
	
print "-------------------------------------------"
disp()

print "Solving the sudoku"
solver(0,0)

disp()
