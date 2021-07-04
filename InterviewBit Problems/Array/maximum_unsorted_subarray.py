# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 15:08:51 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
If A is already sorted, output -1.

Example :
Input 1:
A = [1, 3, 2, 4, 5]
Return: [1, 2]

Input 2:
A = [1, 2, 3, 4, 5]
Return: [-1]

In the above example(Input 1), if we sort the subarray A1, A2, then whole array A should get sorted.
"""

def subUnsort(A):
    end = len(A)-1
    flag = 0
    
    if len(A) > 1:
        for start in range(len(A)-1):
            if A[start] > A[start+1] :
                flag = 1
                break

        if flag==0:
            return [-1]
            
        for j in range(len(A)-1, 0, -1):
            if A[j] < A[j-1]:
                end = j
                break
        
        min_val = min(A[start: end+1])
        max_val = max(A[start: end+1])
        
        #left to right
        for i in range(start):
            if A[i] > min_val:
                start = i
                break
        
        #check right to left
        i = len(A) -1
        while i>=end+1:
            if A[i] < max_val:
                end = i
                break
            i-=1
            
    return [start, end]
    
print(subUnsort([ 1, 2, 3, 5, 6, 13, 15, 16, 17, 13, 13, 15, 17, 17, 17, 17, 17, 19, 19]))