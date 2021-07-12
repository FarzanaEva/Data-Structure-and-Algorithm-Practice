#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-13 03:18:37
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Reverse the bits of an 32 bit unsigned integer A.

Problem Constraints
0 <= A <= 232

Input Format
First and only argument of input contains an integer A.

Output Format
Return a single unsigned integer denoting the decimal value of reversed bits.

Example Input
Input 1:
 0
Input 2:
 3
Example Output
Output 1:
 0
Output 2:
 3221225472

Example Explanation
Explanation 1:
        00000000000000000000000000000000
=>      00000000000000000000000000000000
Explanation 2:
        00000000000000000000000000000011    
=>      11000000000000000000000000000000
"""

def reverse(A):
    rev = 0
    for i in range(32):
        res = A&1
        rev = rev << 1
        rev = rev|res
        A = A >> 1

    return rev
