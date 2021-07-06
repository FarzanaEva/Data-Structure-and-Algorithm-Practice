# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 04:05:50 2021

@author: Farzna Eva
"""
"""
PROBLEM STATEMENT:
Given 2 non negative integers m and n, find gcd(m, n)
GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example
m : 6
n : 9

GCD(m, n) : 3 
NOTE : DO NOT USE LIBRARY FUNCTIONS
"""

def gcd(A, B):
    if A < B: A, B = B, A
    if B == 0:
        return A 
    return gcd(B, A%B)