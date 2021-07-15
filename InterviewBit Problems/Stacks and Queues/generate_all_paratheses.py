#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-16 02:10:11
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""
class Solution:
	# @param A : string
	# @return an integer
	def isValid(self, A):
        stk = []

        for p in A:
            if p == "(" or p=="{" or p == "[":
                stk.append(p)
            else:
                if len(stk) > 0:
                    top = stk.pop()
                    if p == ")" and top != "(": return 0
                    elif p == "}" and top != "{": return 0
                    elif p == "]" and top != "[": return 0
                else:
                    return 0
        
        if len(stk) == 0: return 1
        return 0