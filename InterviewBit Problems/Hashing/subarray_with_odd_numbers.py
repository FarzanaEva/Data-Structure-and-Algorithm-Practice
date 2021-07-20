#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-21 02:46:35
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given an array of integers A and an integer B.
Find the total number of subarrays having exactly B odd numbers.

Problem Constraints
1 <= length of the array <= 105
1 <= A[i] <= 109
0 <= B <= A

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the total number of subarrays having exactly B odd numbers.

Example Input
Input 1:
 A = [4, 3, 2, 3, 4]
 B = 2
Input 2:
 A = [5, 6, 7, 8, 9]
 B = 3

Example Output
Output 1:
 4
Output 2:
 1

Example Explanation
Explanation 1:
 The subarrays having exactly B odd numbers are:
 [4, 3, 2, 3], [4, 3, 2, 3, 4], [3, 2, 3], [3, 2, 3, 4]
Explanation 2:
 The subarrays having exactly B odd numbers is [5, 6, 7, 8, 9]
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        arr = [0] * (len(A) + 1)
        odd = 0

        for i in range(len(A)):
            arr[odd] += 1

            if A[i] % 2 == 1: odd += 1

            if odd >= B: count+= arr[odd-B]

        return count