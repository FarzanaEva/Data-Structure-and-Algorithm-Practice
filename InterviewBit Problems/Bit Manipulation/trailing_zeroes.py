#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-13 02:13:46
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given an integer A, count and return the number of trailing zeroes.

Problem Constraints
1 <= A <= 109

Input Format
First and only argument is an integer A.

Output Format
Return an integer denoting the count of trailing zeroes.

Example Input
Input 1:
 A = 18
Input 2:
 A = 8
Example Output
Output 1:
 1
Output 2:
 3

Example Explanation
Explanation 1:
 18 in binary is represented as: 10010, there is 1 trailing zero.
Explanation 2:
 8 in binary is represented as: 1000, there are 3 trailing zeroes.
 """

def solve(A):
    count = 0
    i = 0

    while(not(A&(1 << i))):
        count+=1
        i+=1

    return count
