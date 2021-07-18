#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-18 01:52:58
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

N Queens: Example 1
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens’ placement, 
where 'Q' and '.' both indicate a queen and an empty space respectively.
For example,
There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        board = [["."]*A for _ in range(A)]

        def isSafePosition(board, x, y):

            for i in range(A):
                for j in range(A):
                    if board[i][j] == "Q":
                        if i == x or j == y or i-j == x-y or x+y == i+j: return False
            return True


        def nQueens(board, row, valid_solution):
            if row == A:
                ans = ["".join(r) for r in board]
                valid_solution.append(ans)
                return

            for col in range(A):
                if isSafePosition(board, row, col):
                    board[row][col] = "Q"
                    nQueens(board, row+1, valid_solution)
                    board[row][col] = "."

            return False

        valid_solution = []
        nQueens(board, 0, valid_solution)

        return valid_solution


print(Solution().solveNQueens(4))
