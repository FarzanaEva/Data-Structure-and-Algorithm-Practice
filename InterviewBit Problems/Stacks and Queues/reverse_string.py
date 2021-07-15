#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-16 01:42:15
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a string S, reverse the string using stack.

Example :
Input : "abc"
Return "cba"
"""

class Solution:
	# @param A : string
	# @return a strings
	def reverseString(self, A):
        if len(A) == 0: return
        stk = []
        rev_str = ""

        for s in A:
            stk.append(s)
        
        while len(stk) > 0:
            rev_str+=stk.pop()

        return rev_str
