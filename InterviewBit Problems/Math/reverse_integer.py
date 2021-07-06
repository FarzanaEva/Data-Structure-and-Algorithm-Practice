# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 03:23:28 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Reverse digits of an integer.
Example1:
x = 123,
return 321
Example2:
x = -123,
return -321
Return 0 if the result overflows and does not fit in a 32 bit signed integer
"""

def reverse(A):
    num = A 
    rev_A = 0
    if A < 0: num*= -1


    while num > 0:
        digit = num % 10
        rev_A = rev_A*10 + digit
        num = num//10

    if A < 0: rev_A *= -1

    if rev_A > (2**31)-1 or rev_A < -(2**31): return 0

    return rev_A