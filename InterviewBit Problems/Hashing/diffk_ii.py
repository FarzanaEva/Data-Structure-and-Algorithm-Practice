#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-19 03:42:55
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Example :
Input :
A : [1 5 3]
k : 2
Output :
1
as 3 - 1 = 2
Return 0 / 1 for this problem.
"""

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
        diff_dict = {}

        for i in range(len(A)):
            if A[i] in diff_dict:
                return 1
            else:
                diff_dict[A[i]-B] = 1
                diff_dict[A[i]+B] = 1

        return 0