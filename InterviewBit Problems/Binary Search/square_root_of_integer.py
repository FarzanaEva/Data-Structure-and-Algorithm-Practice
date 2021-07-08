# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 03:36:14 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT: 
Given an integar A.
Compute and return the square root of A.
If A is not a perfect square, return floor(sqrt(A)).
DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY

Input Format
The first and only argument given is the integer A.
Output Format
Return floor(sqrt(A))
Constraints
1 <= A <= 10^9
For Example
Input 1:
    A = 11
Output 1:
    3
Input 2:
    A = 9
Output 2:
    3
"""

def sqrt(self, A):
    start = 0
    end = A 

    while start <= end:
        mid = start + (end - start)//2

        if mid*mid == A: return mid
        elif mid*mid > A: end = mid - 1
        else: start = mid + 1

    if mid*mid > A: return mid -1
    return mid

print(sqrt(930675566))