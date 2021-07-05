# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 03:32:55 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.
Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.

Input Format:
The first and the only argument of input contains a 2-d integer matrix, A, of size M x N.
Output Format:

Return a 2-d matrix that satisfies the given conditions.
Constraints:
1 <= N, M <= 1000
0 <= A[i][j] <= 1
Examples:

Input 1:
    [   [1, 0, 1],
        [1, 1, 1], 
        [1, 1, 1]   ]

Output 1:
    [   [0, 0, 0],
        [1, 0, 1],
        [1, 0, 1]   ]

Input 2:
    [   [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]   ]

Output 2:
    [   [0, 0, 0],
        [1, 0, 1],
        [0, 0, 0]   ]
"""
def setZeroes(A):
    row_indx = [0]*len(A)
    col_indx = [0]*len(A[0])

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                row_indx[i] = 1
                col_indx[j] = 1


    for i in range(len(A)):
        for j in range(len(A[0])):
            if row_indx[i] or col_indx[j]:
                A[i][j] = 0

    return A

print(setZeroes([[1, 0, 1], [1, 1, 1],[1, 0, 1]]))