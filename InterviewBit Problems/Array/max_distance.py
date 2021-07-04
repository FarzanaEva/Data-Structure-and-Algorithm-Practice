# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 04:46:04 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

Input Format
First and only argument is an integer array A.

Output Format
Return an integer denoting the maximum value of j - i;

Example Input
Input 1:
 A = [3, 5, 4, 2]

Example Output
Output 1:
 2

Example Explanation
Explanation 1:

 Maximum value occurs for pair (3, 4).
"""
def maximumGap(A):
    new_arr = [[x, i] for i, x in enumerate(A)]
    
    new_arr = sorted(new_arr)
    max_val_indx = new_arr[len(new_arr) - 1][1]
    max_diff = 0
    
    for i in range(len(new_arr) - 2, -1, -1):
        max_diff = max(max_diff, max_val_indx - new_arr[i][1])
        max_val_indx = max(max_val_indx, new_arr[i][1])
    
    return max_diff
    
 
print(maximumGap([ 3, 2, 1 ]))