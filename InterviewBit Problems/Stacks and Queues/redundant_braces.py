#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-16 03:00:33
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a string A denoting an expression. It contains the following operators ’+’, ‘-‘, ‘*’, ‘/’.
Chech whether A has redundant braces or not.
Return 1 if A has redundant braces, else return 0.
Note: A will be always a valid expression.

Input Format
The only argument given is string A.

Output Format
Return 1 if string has redundant braces, else return 0.
For Example
Input 1:
    A = "((a + b))"
Output 1:
    1
    Explanation 1:
        ((a + b)) has redundant braces so answer will be 1.

Input 2:
    A = "(a + (a + b))"
Output 2:
    0
    Explanation 2:
        (a + (a + b)) doesn't have have any redundant braces so answer will be 0.
"""

class Solution:
	# @param A : string
	# @return an integer
	def braces(self, A):
        stk = []
        for i in range(len(A)):
            opt_flag = 0
            if A[i] != ")": stk.append(A[i])
            elif A[i] == ")":
                last = stk.pop()
                if last == "(": return 1
                else:
                    while last!="(":
                        if last in "+-*/": opt_flag = 1
                        last = stk.pop()

                    if not opt_flag: return 1

        return 0
