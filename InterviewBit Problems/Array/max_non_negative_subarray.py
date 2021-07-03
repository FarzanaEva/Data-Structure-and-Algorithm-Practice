# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 03:08:26 2021

@author: Farzana Eva
"""

"""
PROBLEM STATEMENT:
Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.
The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.
Maximum sub-array is defined in terms of the sum of the elements in the sub-array.
Find and return the required subarray.

NOTE:  
If there is a tie, then compare with segment's length and return segment which has maximum length.
If there is still a tie, then return the segment with minimum starting index.

Problem Constraints
1 <= N <= 10^5
-10^9 <= A[i] <= 10~9

Input Format
The first and the only argument of input contains an integer array A, of length N.

Output Format
Return an array of integers, that is a subarray of A that satisfies the given conditions.

Example Input
Input 1:
A = [1, 2, 5, -7, 2, 3]
Input 2:
A = [10, -1, 2, 3, -4, 100]

Example Output
Output 1:
 [1, 2, 5]
Output 2:
 [100]
"""

def maxset(A):
    start_ind, end_ind = -1, -1
    start , end = 0, -1
    max_sum , sum_arr = 0, 0
    count, max_count = 0, 0
    i = 0

    while i < len(A):
        if A[i] >= 0:
            sum_arr += A[i]
            count +=1
            end +=1
        
        if sum_arr > max_sum:
            max_sum = sum_arr
            start_ind = start
            end_ind = end
        
        elif max_sum == sum_arr and count > max_count:
            max_count = count
            start_ind = start
            end_ind = end
        
        if A[i] < 0:
            sum_arr = 0
            count = 0
            end = i
            start = i+1

        i += 1

    if start_ind== -1 and end_ind == -1: return []
    return A[start_ind: end_ind+1]


print(maxset([1, 2, 5, -7, 2, 3]))