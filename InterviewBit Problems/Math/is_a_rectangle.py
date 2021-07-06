# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 02:50:46 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:

Given four positive integers A, B, C, D, determine if there’s a rectangle such that the lengths of its sides are A, B, C and D (in any order).
If any such rectangle exist return 1 else return 0.

Problem Constraints
1 <= A, B, C, D <= 100

Input Format
First argument is an interger A.
Second argument is an interger B.
Third argument is an interger C.
Fourth argument is an interger D.

Output Format
If any such rectangle exist whose sides are A, B, C, D in any orde then return 1 else return 0.

Example Input
Input 1:
 A = 1
 B = 1
 C = 2
 D = 2
Input 2:
 A = 1
 B = 2
 C = 3
 D = 4

Example Output
Output 1:
 1
Output 2:
 0
"""

def solve(self, A, B, C, D):
    if A > 0 and B > 0 and C > 0 and D > 0:
        if A - B == 0 and C - D == 0:
            return 1       
        if A - C == 0 and B - D == 0:
            return 1      
        if A - D == 0 and B - C == 0:
            return 1

    return 0
