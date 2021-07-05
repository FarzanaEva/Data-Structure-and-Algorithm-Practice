# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 02:58:36 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:		
Input: 	
1 2 3
4 5 6
7 8 9

Return the following :
[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]
Input : 
1 2
3 4
Return the following  : 
[
  [1],
  [2, 3],
  [4]
]
"""

def diagonal(A):
    anti_diagonal = [[] for i in range(2*len(A) - 1)]

    for i in range(len(A)):
        for j in range(len(A)):
            anti_diagonal[i+j].append(A[i][j])


    return anti_diagonal

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal(A))