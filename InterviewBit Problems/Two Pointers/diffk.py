# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 03:24:59 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given an array ‘A’ of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
Example:
Input :
    A : [1 3 5] 
    k : 4
Output : YES
as 5 - 1 = 4
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
Try doing this in less than linear space complexity.
"""

def diffPossible(A, B):
    i = 0
    j = 1

    while i < len(A) and j < len(A):
        if i!=j and A[j] - A[i] == B: return 1
        elif A[j] - A[i] < B: j +=1
        else: i+=1

    return 0