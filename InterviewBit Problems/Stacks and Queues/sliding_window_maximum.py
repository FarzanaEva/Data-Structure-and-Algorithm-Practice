#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-16 04:27:14
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given an array of integers A.  There is a sliding window of size B which 
is moving from the very left of the array to the very right. 
You can only see the w numbers in the window. Each time the sliding window moves 
rightwards by one position. You have to find the maximum for each window. 
The following example will give you more clarity.
The array A is [1 3 -1 -3 5 3 6 7], and B is 3.

Window position	Max
———————————-	————————-
[1  3  -1] -3  5  3  6  7	3
1 [3  -1  -3] 5  3  6  7	3
1  3 [-1  -3  5] 3  6  7	5
1  3  -1 [-3  5  3] 6  7	5
1  3  -1  -3 [5  3  6] 7	6
1  3  -1  -3  5 [3  6  7]	7
Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].
Note: If B > length of the array, return 1 element with the max of the array.

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.

Output Format
Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1]
For Example
Input 1:
    A = [1, 3, -1, -3, 5, 3, 6, 7]
    B = 3
Output 1:
    C = [3, 3, 5, 5, 6, 7]
"""

import collections

class Solution:
    # @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
    def slidingMaximum(self, A, B):
        left = 0
        right = 0
        max_arr = []
        que = collections.deque()

        while right < len(A):
            while que and A[right] > A[que[-1]]:
                que.pop()
            que.append(right)

            #pop if there is any min value at front which is out of the window
            if left > que[0]: que.popleft()

            if right+1 >= B:
                max_arr.append(A[que[0]])
                left += 1
            right +=1

        return max_arr