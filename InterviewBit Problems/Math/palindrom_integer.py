# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 03:22:01 2021

@author: FarZa
"""
"""
PROBLEM STATEMENT:

Determine whether an integer is a palindrome. Do this without extra space.
A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.

Example :
Input : 12121
Output : True

Input : 123
Output : False
"""

def isPalindrome(A):
    num = A
    rev_A = 0

    while num > 0:
        digit = num % 10
        rev_A = rev_A*10 + digit
        num = num // 10

    if A == rev_A: return 1

    return 0