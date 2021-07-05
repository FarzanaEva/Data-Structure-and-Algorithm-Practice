# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 02:07:37 2021

@author: Farzana Eva
"""

"""
PROBLEM STATEMENT:
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
You need to do this in place.
Note that if you end up using an additional array, you will only receive partial score.

Example:
If the array is
[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:
[
    [3, 1],
    [4, 2]
]
"""

def rotate(A):
    for i in range(len(A)):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
            
            
    for i in range(len(A)):
        for j in range(len(A)//2):
            A[i][j], A[i][len(A)-j-1] = A[i][len(A)-j-1], A[i][j]
            
    return A

print(rotate([[1, 2, 3], [4, 5, 6], [7, 8,9]]))