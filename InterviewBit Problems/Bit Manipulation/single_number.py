#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-13 02:41:40
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given an array of integers, every element appears twice except for one. Find that single one.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Input Format:
    First and only argument of input contains an integer array A
Output Format:
    return a single integer denoting single element

Constraints:
2 <= N <= 2 000 000  
0 <= A[i] <= INT_MAX

For Examples :
Example Input 1:
    A = [1, 2, 2, 3, 1]
Example Output 1:
    3
Explanation:
    3 occurs only once
Example Input 2:
    A = [1, 2, 2]
Example Output 2:
    1
"""

def singleNumber(A):
    num = A[0]
    
    for i in range(1, len(A)):
        num = num^A[i]

    return num
