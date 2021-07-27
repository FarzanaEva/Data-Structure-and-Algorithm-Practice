#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-27 22:42:56
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
You are climbing a stair case and it takes A steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input Format:
The first and the only argument contains an integer A, the number of steps.
Output Format:
Return an integer, representing the number of ways to reach the top.

Constrains:
1 <= A <= 36

Example :
Input 1:
A = 2 Output 1:
2 Explanation 1:
[1, 1], [2] Input 2:
A = 3 Output 2:
3 Explanation 2: 
[1 1 1], [1 2], [2 1]
"""

memo = [0] * 37
class Solution:
	# @param A : integer
	# @return an integer
	def climbStairs(self, A):
        if A == 0 or A == 1: return 1

        if memo[A]!= 0: return memo[A]

        memo[A] = self.climbStairs(A-1)+self.climbStairs(A-2)

        return memo[A]