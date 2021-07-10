# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 01:52:10 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given an integer A, convert it to a roman numeral, and return a string corresponding to its roman numeral version
Note : This question has a lot of scope of clarification from the interviewer. Please take a moment to think of all the needed clarifications and see the expected response using “See Expected Output”
For the purpose of this question, https://projecteuler.net/about=roman_numerals has very detailed explanations.

Input Format
The only argument given is integer A.
Output Format
Return a string denoting roman numeral version of A.
Constraints
1 <= A <= 3999
For Example
Input 1:
    A = 5
Output 1:
    "V"
Input 2:
    A = 14
Output 2:
    "XIV"
"""

def intToRoman(A):
    roman = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40:"XL", 50: "L", 
    90: "XC", 100: "C", 400: "CD", 500:"D", 900: "CM", 1000:"M"}

    if A in roman: return roman[A]

    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_str = ""

    while A > 0:
        for d in num:
            quo = A//d
            
            if quo!= 0: roman_str+= quo*roman[d]

            A = A% d

    return roman_str
