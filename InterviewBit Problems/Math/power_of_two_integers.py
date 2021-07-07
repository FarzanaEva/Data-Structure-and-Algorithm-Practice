# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 00:26:45 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

Example
Input : 4
Output : True  
as 2^2 = 4. 
"""

def isPower(A):
    if A == 1: return 1

    for i in range(2, 32):
        r = round(A**(1/i))

        if r**i == A: return 1
    
    return 0