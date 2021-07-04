# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 20:24:21 2021

@author: Farzana Eva
"""

"""
PROBLEM STATEMENT:
Given numRows, generate the first numRows of Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:
Given numRows = 5,
Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
"""

def pascalTriangle(A):
    pascal = []
    
    for i in range(A):
        arr = [1]*(i+1)
        
        j = 1
        k = i
        
        while j < k:
            arr[j] = pascal[i-1][j] + pascal[i-1][j-1]
            arr[i - j] = arr[j]
        
            j+= 1
            k -= 1
        
        
        pascal.append(arr)
        
    return pascal


print(pascalTriangle(8))
        