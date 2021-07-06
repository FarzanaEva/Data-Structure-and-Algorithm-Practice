# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 04:07:52 2021

@author: Farzana Eva
"""

"""
PROBLEM STATEMENT:
Given a number N >= 0, find its representation in binary.

Example:
if N = 6,

binary form = 110
"""

def findDigitsInBinary(A):
    binary = ""
    
    if A == 0: return 0

    while A > 0:
        remainder = A%2
        A = A // 2

        binary += str(remainder)

    
    return binary[::-1]


