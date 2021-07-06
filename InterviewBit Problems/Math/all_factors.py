# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 04:10:49 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a number N, find all factors of N.

Example:

N = 6 
factors = {1, 2, 3, 6}
Make sure the returned array is sorted.
"""

def allFactors(A):
    factors = []
    if A == 1: return [1]
    for i in range(1,int(A**0.5)+1):
        if A%i == 0:
            factors.append(i)
            if i != A//i:
                factors.append(A//i)

    return sorted(factors)