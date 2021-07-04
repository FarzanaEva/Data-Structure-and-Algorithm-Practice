# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 23:12:22 2021

@author: Farzana Eva
"""

def generateMatrix(A):
    top, bottom = 0, A-1
    left, right = 0, A-1
    val = 1
    direction = 1
    
    matrix = [[0]*A for i in range(A)]
    
    while val <= A*A:  
        if direction == 1: #left -> right
            for i in range(left, right+1):
                matrix[top][i] = val
                val += 1
                
            top += 1
            direction = 2
            
        elif direction == 2: #top -> bottom
            for i in range(top, bottom+1):
                matrix[i][right] = val
                val += 1
                
            right -= 1
            direction = 3
            
        elif direction == 3: #right -> left
            for i in range(right, left - 1, -1): 
                matrix[bottom][i] = val
                val+= 1
            
            bottom -= 1
            direction = 4
            
        elif direction == 4: #bottom -> top
            for i in range(bottom, top -1, -1):
                matrix[i][left] = val
                val += 1
                
            left += 1
            direction = 1
            
    return matrix


print(generateMatrix(3))