from sudoku_create import sudoku,disp
count=0
stack=[]
def solver(first,backtrack):
	global stack,count
	val_assign=0
	while(first<81):
		row=first/9
		column=first%9
		if(sudoku[row][column]==0 or backtrack==1):
			backtrack=0
			for val_assign in range(sudoku[row][column]+1,11):
				assign1=1		
				if(val_assign>9):
					count=count+1
					backtrack=1
					sudoku[row][column]=0
					nsum=stack.pop()
					first=nsum-1
					break
				for column1 in range(0,9):
					if(val_assign==sudoku[row][column1]):
						assign1=0
						break
				if(assign1==1):
					for row1 in range(0,9):
						if(val_assign==sudoku[row1][column]):
							assign1=0
							break
				if(assign1==1):
					for row1 in range(int(row/3)*3,(int((row/3)*3)+3)):
						for column1 in range(int(column/3)*3,(int((column/3)*3)+3)):
							if(val_assign==sudoku[row1][column1]):
								assign1=0
								break
				if(assign1==1):
					sudoku[row][column]=val_assign
					stack.append(first)
					break
		print "Stack: ",stack
		print "Value assigned: ",val_assign
		
		first=first+1
	print "No of backtracks: ",count	
	return
