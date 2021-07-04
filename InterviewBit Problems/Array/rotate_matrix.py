# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 02:07:37 2021

@author: Farzana Eva
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