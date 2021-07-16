#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-17 04:14:47
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Implement pow(A, B) % C.
In other words, given A, B and C, 
find (A^B)%C.

Input : A = 2, B = 3, C = 3
Return : 2 
2^3 % 3 = 8 % 3 = 2
"""

class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @return an integer
    def Mod(self, A, B, C):
        if A == 0: return 0
        if B == 0: return 1

        if B%2 == 0:
            modulus = self.Mod(A, B//2, C)
            return (modulus*modulus) % C 
        else: return ((A%C) * self.Mod(A, B-1, C))


