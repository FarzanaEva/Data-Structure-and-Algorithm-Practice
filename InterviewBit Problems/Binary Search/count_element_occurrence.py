# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:28:34 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a sorted array of integers, find the number of occurrences of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return 0
**Example : **
Given [5, 7, 7, 8, 8, 10] and target value 8,
return 2.
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        indx = self.binarySearch(A, B)
        
        if indx == -1: return 0
    
        count = 1
        left = indx - 1
    
        while left >= 0:
            if A[left] == B: count+=1
            if A[left] < B: break
            left -=1
    
        right = indx + 1
        while right< len(A):
            if A[right] == B: count+=1
            if A[right] > B: break
            right +=1
    
        return count

    def binarySearch(self, A, B):
        start = 0
        end = len(A) - 1
    
        while start<= end:
            mid = (start+end) //2
    
            if A[mid] == B: return mid
            elif A[mid] > B: end = mid - 1
            else: start = mid+1
    
        return -1

