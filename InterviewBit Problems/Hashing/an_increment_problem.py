#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-21 04:02:40
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a stream of numbers A. On arrival of each number, you need to increase its first occurence by 1 and include this in the stream.
Return the final stream of numbers.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10000

Input Format
First and only argument is the array A.

Output Format
Return an array, the final stream of numbers.

Example Input
Input 1:
A = [1, 1]
Input 2:
A = [1, 2]

Example Output
Output 1:
[2, 1]
Output 2:
[1, 2]

Example Explanation
Explanation 1:
 On arrival of the second element, the other element is increased by 1.
Explanation 2:
No increases are to be done.
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        new_strm = []

        for i in range(len(A)):
            for j in range(len(new_strm)):
                if A[i] == new_strm[j]:
                    new_strm[j] += 1
                    break
            new_strm.append(A[i])

        return new_strm    