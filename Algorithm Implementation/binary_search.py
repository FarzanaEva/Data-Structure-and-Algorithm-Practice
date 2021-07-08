# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 21:40:51 2021

@author: Farzana Eva
"""

#iterative approach
def binarySearch(A, num):
    start = 0
    end = len(A)-1
    
    while start <= end:
        mid = (start+end)//2 
        
        if A[mid] == num: return mid
        elif A[mid] > num: end = mid - 1
        else: start = mid + 1
        
    return -1

print("Iterative Approach: ",binarySearch([1, 4, 7, 10, 15, 23, 40, 75], 20))


#recursive approach
def binary_search(A, start, end, num):
    if start > end: return -1
    
    mid = (start+end) // 2    
    if A[mid] == num: return mid
    elif A[mid] > num: return binary_search(A, start, mid-1, num)
    else: return binary_search(A, mid+1, end, num)
    


A = [1, 4, 7, 10, 15, 23, 40, 75]
start = 0
end = len(A) - 1   
print("Recursive Approach", binary_search(A, start, end, 23))
