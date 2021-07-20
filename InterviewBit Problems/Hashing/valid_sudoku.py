#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-21 04:51:27
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.
The input corresponding to the above configuration :
["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""

class Solution:
	# @param A : tuple of strings
	# @return an integer
    def isValidSudoku(self, A):
        for i in range(len(A)):
            for j in range(len(A)):
                if not (self.isNotInRow(A,i) and self.isNotInCol(A, j) and self.isNotInBox(A, i-i%3, j-j%3)):
                    return 0

        return 1

    def isNotInRow(self, A, row):
        row_set = set()
        for i in range(len(A[row])):
            if A[row][i]!= ".":
                if A[row][i] not in row_set:
                    row_set.add(A[row][i])
                else: return False
        return True
    
    def isNotInCol(self, A, col):
        col_set = set()
        for i in range(len(A)):
            if A[i][col] in col_set: return False
            if A[i][col]!= '.': col_set.add(A[i][col])
        return True

    def isNotInBox(self, A, row, col):
        box_Set = set()
        for i in range(3):
            for j in range(3):
                if A[i+row][j+col] in box_Set: return False
                if A[i+row][j+col]!= ".": box_Set.add(A[i+row][j+col])
        
        return True
    
print(Solution().isValidSudoku(["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]))
