# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 01:23:12 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.
Note that even though we want you to return the new length, make sure to change the original array as well in place
Do not allocate extra space for another array, you must do this in place with constant memory.
Example: 
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
"""

def removeDuplicates(A):
    if len(A) == 0: return 0
    i = 0
    j = 1

    while j < len(A):
        if A[i] == A[j]: j+=1
        else:
            i+=1
            A[i] = A[j]
    return i+1

A = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ]
ind = removeDuplicates(A)
print(ind)
print(A[:ind])