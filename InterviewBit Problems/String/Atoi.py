# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 05:33:01 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
There are certain questions where the interviewer would intentionally frame the question vague.
The expectation is that you will ask the correct set of clarifications or state your assumptions before you jump into coding.
Implement atoi to convert a string to an integer.

Example :
Input : "9 2704"
Output : 9
Note: There might be multiple corner cases here. Clarify all your doubts using “See Expected Output”.
Questions:
Q1. Does string contain whitespace characters before the number?
A. Yes
Q2. Can the string have garbage characters after the number?
A. Yes. Ignore it.
Q3. If no numeric character is found before encountering garbage characters, what should I do?
A. Return 0.
Q4. What if the integer overflows?
A. Return INT_MAX if the number is positive, INT_MIN otherwise.
Warning : DO NOT USE LIBRARY FUNCTION FOR ATOI.
If you do, we will disqualify your submission retroactively and give you penalty points.
"""

def atoi(A):
    num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    neg = 1
    integer = 0
    
    for i in range(len(A)):
        if A[i] in "+-0123456789":
            if i > 0 and A[i-1] == '-': neg = -1
            if A[i] in num:
                integer = 10*integer + num[A[i]]
        else: break
    
    if integer*neg > 2**31 -1 : return 2**31 -1
    elif integer*neg < -2**31: return -2**31
    return integer*neg