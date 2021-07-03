# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 03:04:36 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example:
Given the following matrix:
[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
You should return
[1, 2, 3, 6, 9, 8, 7, 4, 5]
"""

def spiralOrder(A):
    top = 0 #row start
    bottom = len(A) - 1 #row end
    left = 0 #col start
    right = len(A[0])-1 #col end
    direction = 0 
    spiral = []

    while(top <= bottom and left <= right):
        if direction == 0 : #left -> right
            for i in range(left, right+1):
                spiral.append(A[top][i])
            top +=1
            direction = 1
        
        elif direction == 1: #top -> bottom
            for i in range(top, bottom+1):
                spiral.append(A[i][right])
            
            right -= 1
            direction = 2
        
        elif direction == 2: #right -> left
            for i in range(right, left-1, -1):
                spiral.append(A[bottom][i])
            
            bottom -= 1
            direction = 3

        elif direction == 3: # bottom -> top
            for i in range(bottom, top-1, -1):
                spiral.append(A[i][left])
            
            left += 1
            direction = 0
    
    return spiral


arr = [[ 1, 2, 3 ],
       [ 4, 5, 6 ],
       [ 7, 8, 9 ]]

print(spiralOrder(arr))