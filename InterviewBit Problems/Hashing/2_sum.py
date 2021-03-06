#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-20 00:10:27
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based. 
Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.
If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2
"""

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def twoSum(self, A, B):
        indices = []

        sum_arr = {}

        for i in range(len(A)):
            if A[i] in sum_arr:
                indices.append(sum_arr[A[i]])
                indices.append(i+1)
                return indices
            else:
                if B-A[i] not in sum_arr: 
                    sum_arr[B-A[i]] = i+1

        return indices