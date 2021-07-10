# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 01:48:18 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a string A representing a roman numeral.
Convert A into integer.
A is guaranteed to be within the range from 1 to 3999.
NOTE: Read more 
details about roman numerals at Roman Numeric System

Input Format
The only argument given is string A.
Output Format
Return an integer which is the integer verison of roman numeral string.
For Example
Input 1:
    A = "XIV"
Output 1:
    14
Input 2:
    A = "XX"
Output 2:
    20
"""
def romanToInt(A):
    num = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for i in range(len(A)-1):
        if roman[A[i]] < roman[A[i+1]]:
            num -= roman[A[i]]
        else:
            num+= roman[A[i]]
    num += roman[A[len(A)-1]]
    return num



