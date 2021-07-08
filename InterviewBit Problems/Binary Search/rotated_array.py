# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 03:51:38 2021

@author: Farzana Eva
"""

"""
PROBLEM STATEMENT:
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
The array will not contain duplicates.
NOTE 1: Also think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
PROBLEM APPROACH:
Note: If you know the number of times the array is rotated, then this problem becomes trivial. If the number of rotation is x, then minimum element is A[x].
Lets look at how we can calculate the number of times the array is rotated.
Complete solution in the hints.
"""
def findMin(A):
    if len(A) == 1: return A[0]
    if A[0] < A[-1]: return A[0]

    start = 0
    end = len(A) - 1

    while start <= end:
        mid = start + (end -start)//2

        if A[start] > A[mid]:
            if A[mid-1] > A[mid]: return A[mid]
            end = mid - 1
        else:
            if A[mid] > A[mid+1]: return A[mid+1]
            start = mid+1

    return A[start]


