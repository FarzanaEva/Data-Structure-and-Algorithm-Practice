# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 03:09:57 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given integar B in array A.
Your algorithm’s runtime complexity must be in the order of O(log n).
Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].

Input Format

The first argument given is the integer array A.
The second argument given is the integer B.
Output Format

 Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].
Constraints

1 <= N <= 10^6
1 <= A[i], B <= 10^9
For Example

Input 1:
    A = [5, 7, 7, 8, 8, 10]
    B = 8
Output 1:
    [3, 4]
Explanation 1:
    First occurence of 8 in A is at index 3
    Second occurence of 8 in A is at index 4
    ans = [3, 4]

Input 2:
    A = [5, 17, 100, 111]
    B = 3
Output 2:
    [-1, -1]
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        mid = self.binary_search(A, B)
        print(mid)
        if mid!= -1:
            start = -1; end = -1
            left = mid-1
            while left >=0:
                if A[left] == B: start = left
                elif A[left]!= B: break
                left -=1
            
            for i in range(mid+1, len(A)):
                if A[i] == B: end = i
                elif A[i]!= B: break

            if start == -1: start = mid
            if end == -1: end = mid

            return [start, end]
        return [-1, -1]

    def binary_search(self, A, B):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start+end)//2
            print(mid)
            if A[mid] == B: return mid
            elif A[mid] > B: end = mid - 1
            else: start = mid + 1

        return -1
    
A = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]
B = 10
print(Solution().searchRange(A, B))