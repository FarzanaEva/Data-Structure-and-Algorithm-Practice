# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 02:35:49 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
"""
def solve(A, B):
    diff_dict = {}

    for i in range(len(A)):
        if A[i] in diff_dict: return 1
        else:
            diff_dict[A[i]+B] = A[i]
            diff_dict[A[i]-B] = A[i]
        
    return 0

A = [ 90, 497, -411, 990, 145, 353, 314, -349, -260, -956, 258, -665, -241, 192, 605, 264, -819, -497, 829, 775, -392, 292, 997, 549, 556, 561, 627, -533, 541, -871, 240, 813, 174, -399, -923, -785 ]
B = -466

print(solve(A, B))