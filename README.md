# SUDOKU-using-Backtracking

## Introduction

The long and interesting history of the Sudoku is quite a puzzle in itself. The name “Sudoku” comes from Japan and consists of the Japanese characters Su (meaning 'number') and Doku (meaning 'single') but the was not invented in Japan. Sudoku originated in Switzerland and then travelled to Japan by way of America. Sudoku has its deep roots in ancient number puzzles. For many centuries people have been interested in creating and solving them. Puzzles continue to stimulate new development in mathematics, as you can see in the film “A Beautiful Mind”.


## Rules of Sudoku

Solving a sudoku puzzle can be rather tricky, but the rules of the game are quite simple. A sudoku puzzle is a grid of nine by nine squares or cells, that has been subdivided into nine subgrids or "regions" of three by three cells.

The objective of sudoku is to enter a digit from 1 through 9 in each cell, in such a way that:
•	Each horizontal row (shown in pink) contains each digit exactly once
•	Each vertical column (shown in yellow) contains each digit exactly once
•	Each sub grid or region (shown in green) contains each digit exactly once

## Algorithm Used

•	Backtracking:

	Have used the Backtracking approach to solve the Sudoku puzzle. Also have implemented an algorithm for creating a valid Sudoku puzzle by itself. It has 2 levels of difficulties: 
•	Easy (the given number of values would be around 35) and 
•	Hard (the given number of values would be around 20) and 
•	also have given a provision wherein the user may give his own Sudoku input values to be solved by our program.

	Backtracking algorithms are adapted to solve the Sudoku that iterates through all the possible solutions for the given sudoku. If the solutions assigned do not lead to the solution of Sudoku, the algorithm discards the solutions and rollbacks to the original solutions and retries again and hence the name backtracking. 

Initialize 2D array with 81 empty grids (nx = 9, ny = 9)
 Fill in some empty grid with the known values
 Make an original copy of the array
 Start from top left grid (nx = 0, ny = 0), check if grid is empty
 if (grid is empty) {
   assign the empty grid with values (i)
   if (no numbers exists in same rows & same columns same as (i) & 3x3 square (i) is currently in)
     fill in the number
   if (numbers exists in same rows & same columns same as (i) & 3x3 square (i) is currently in)
     discard (i) and repick other values (i++)
 }
 else {
   while (nx < 9) {
     Proceed to next row grid(nx++, ny)
     if (nx equals 9) {
       reset nx = 1
       proceed to next column grid(nx,ny++)
       if (ny equals 9) {
         print solution
       }
     }
   }
 }

## Programming Language Used: Python

## File Names
1.	sudoku_create.py
2.	sudoku_solver.py
3.	sudoku_AI.py

*To run the program, change the directory to which all the files are present in and type this com-mand: 
python sudoku_AI.py


•	Solving a Sudoku of arbitrary rank n is a much more difficult problem. As the rank of a Su-doku increases from n to n+1, the extra computational time needed to find a solution in-creases quite fast. This places the game of solving rank-n Sudoku puzzles in a class of prob-lems that computer scientists have named NP-complete. An NP-complete problem satisfies the following two properties:

1.	Any solution to the problem can be checked relatively quickly, i.e. in polynomial time.

2.	If the problem can be solved relatively quickly, then so can every problem that satis-fies property (1).

## Fun Fact

•	First World Sudoku championship was held in Italy in 2006. After that, in 2007 in Prague, Czech Republic and in 2008 it was held in Goa, India!
