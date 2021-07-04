# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 22:27:57 2021

@author: Farzana
"""
"""
PROBLEM STATEMENT:
Given an index k, return the kth row of the Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:
Input : k = 3
Return : [1,3,3,1]
NOTE : k is 0 based. k = 0, corresponds to the row [1].

Note:Could you optimize your algorithm to use only O(k) extra space?
"""


def getRow(A):
    prev_row =  [1]
    for i in range(A+1):
        curr_row = [1]*(i+1)
        
        j = 1
        k = i
        
        while j < k:
            curr_row[j] = prev_row[j] + prev_row[j-1]
            curr_row[i-j] = curr_row[j]
            j +=1
            k -=1
        prev_row = curr_row
        
    return prev_row

print(getRow(7))
        
        
        
        