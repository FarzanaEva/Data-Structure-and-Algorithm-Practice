#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-20 05:06:31
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given an array of integers A and an integer B.
Find the total number of subarrays having bitwise XOR of all elements equals to B.

Problem Constraints
1 <= length of the array <= 105
1 <= A[i], B <= 109

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the total number of subarrays having bitwise XOR equals to B.

Example Input
Input 1:
 A = [4, 2, 2, 6, 4]
 B = 6
Input 2:
 A = [5, 6, 7, 8, 9]
 B = 5

Example Output
Output 1:
 4
Output 2:
 2

Example Explanation
Explanation 1:
 The subarrays having XOR of their elements as 6 are:
 [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]
Explanation 2:
 The subarrays having XOR of their elements as 2 are [5] and [5, 6, 7, 8, 9]

"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        arr_dict = {}
        count = 0
        num = 0
        arr_dict[0] = 1

        for i in range(len(A)):
            num ^= A[i]

            if num^B in arr_dict:
                count += arr_dict[num^B]
            if num in arr_dict:
                arr_dict[num] += 1
            else: arr_dict[num] = 1

        return count

