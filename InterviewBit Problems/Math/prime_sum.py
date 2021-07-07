# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 02:07:28 2021

@author: FarZa
"""
"""
PROBLEM STATEMENT:
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
NOTE A solution will always exist. read Goldbach’s  conjecture

Example:
Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.
If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then
[a, b] < [c, d] 
If a < c OR a==c AND b < d.
"""

def primesum(A):
    flag = 0
    for i in range(2, A//2+1):
        diff = A - i
        flag = 0
        for j in range(2, int(diff**0.5)+1):
            if diff%j == 0 or (i%j==0 and i!=j):
                flag = 1
                break
        if not flag: return i, diff
        

print(primesum(1048574))