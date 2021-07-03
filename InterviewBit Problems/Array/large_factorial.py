# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 03:14:16 2021

@author: Farzana Eva
"""

"""
PROBLEM STATEMENT:
Given a number A. Find the fatorial of the number.

Problem Constraints
1 <= A <= 100

Input Format
First and only argument is the integer A.

Output Format
Return a string, the factorial of A.

Example Input
Input 1:
A = 2
Input 2:
A = 3

Example Output
Output 1:
 2
Output 2:
 6
"""

def solve(A):
    fact_arr = 1
    for i in range(A):
        fact_arr *= (i+1)
    return fact_arr

print(solve(100))