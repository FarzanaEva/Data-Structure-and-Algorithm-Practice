# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 01:39:55 2021

@author: Farzana Eva
"""

"""
PROBLEM STATEMENT:
Remove Duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
Note that even though we want you to return the new length, make sure to change the original array as well in place
For example,
Given input array A = [1,1,1,2],
Your function should return length = 3, and A is now [1,1,2].
"""
def removeDuplicates(A):
    if len(A) == 0: return 0
    cnt = 1
    i = 0
    j = 1

    while j < len(A):
        if A[i] == A[j]:
            cnt+=1
            if cnt <= 2 and A[i]== A[i+1]: i+=1
            elif cnt ==2 and A[i]!=A[i+1]: 
                A[i+1] = A[i]
                i+=1
            j+=1
        else:
            i+=1
            A[i] = A[j]
            cnt = 1
            j += 1
    
    return i+1

