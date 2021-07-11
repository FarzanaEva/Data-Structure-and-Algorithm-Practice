# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 22:24:16 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given an array with n objects colored red, white or blue, 
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: Using library sort function is not allowed.
Example :
Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
"""

def sortColors(A):
    j = 0
    for clr in range(3):
        for i in range(j, len(A)):
            if A[i] == clr:
                A[i], A[j] = A[j], A[i]
                j+=1

    return A
