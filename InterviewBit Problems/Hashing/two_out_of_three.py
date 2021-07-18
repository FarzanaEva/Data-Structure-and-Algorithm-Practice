#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-19 03:44:40
# @Author  : Farzana Eva 
# @Version : 1.0.0

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        A = list(set(A))
        B = list(set(B))
        c = list(set(C))

        arr_dict = {}
        res = []

        for i in range(len(A)):
            arr_dict[A[i]] = 1

        for i in range(0, len(B)):
            if B[i] in arr_dict:
                arr_dict[B[i]] += 1
            else:
                arr_dict[B[i]] = 1

        for i in range(0, len(C)):
            if C[i] in arr_dict:
                arr_dict[C[i]] += 1

        
        for key, val in arr_dict.items():
            if val> 1: res.append(key)

        return sorted(res)
