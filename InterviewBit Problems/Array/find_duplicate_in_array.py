# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 02:09:34 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.

Sample Input:
[3 4 1 4 1]
Sample Output:
1
If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1
"""

def repeatedNumber(A):
    
    #time complexity : O(n), space complexity : O(n)
    num = {}

    for i in range(len(A)):
        if A[i] in num:
            return A[i]
        else:
            num[A[i]] = 1
    
    return -1

    
print(repeatedNumber([3, 4, 1, 4, 1]))