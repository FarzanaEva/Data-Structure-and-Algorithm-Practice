# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 20:15:23 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.
Example :
Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]
Output : [3 3 5]
Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 5]
Output : [3 5]
NOTE : For the purpose of this problem ( as also conveyed by the sample case ), assume that elements that appear more than once in both arrays should be included multiple times in the final output.
"""

def intersect(A, B):
    if len(A) == 1 and len(B) == 1 and A==B: return A
    if len(A) == 0 or len(B) == 0: return []

    i = 0
    j = 0
    intersect = []

    while j < len(B) and i< len(A):
        if A[i] == B[j]:
            intersect.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]: i +=1
        else: j += 1
        
    return intersect

A = [ 12, 30, 41, 51, 56, 58, 63, 67, 82, 90, 93 ]
B = [ 7, 9, 17, 17, 19, 21, 26, 34, 65, 65, 67, 68, 71, 75, 92 ]
print(intersect(A, B))