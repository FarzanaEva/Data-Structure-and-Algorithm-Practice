#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-20 02:57:53
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given an integer array A of size N containing 0's and 1's only. 
You need to find the length of the longest subarray having count of 1’s one more than count of 0’s.

Problem Constraints
1 <= N <= 105

Input Format
First and only argument is an integer array A of size N.

Output Format
Return an integer denoting the longest length of the subarray.

Example Input
Input 1:
 A = [0, 1, 1, 0, 0, 1]
Input 2:
 A = [1, 0, 0, 1, 0]

Example Output
Output 1:
 5
Output 2:
 1

Example Explanation
Explanation 1:
 Subarray of length 5, index 1 to 5 i.e 1, 1, 0, 0, 1. Count of 1 = 3, Count of 0 = 2.
Explanation 2:
 Subarray of length 1 will be only subarray that follow the above condition.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        sum_val = 0
        max_len = 0

        arr_dict ={}

        for i in range(len(A)):
            if A[i] == 0:
                sum_val -= 1
            else: sum_val +=1

            if sum_val == 1: max_len = i+1
            elif sum_val not in arr_dict:
                arr_dict[sum_val] = i

            if sum_val-1 in arr_dict:
                if (i - arr_dict[sum_val-1]) > max_len:
                    max_len = i - arr_dict[sum_val-1]

        return max_len
