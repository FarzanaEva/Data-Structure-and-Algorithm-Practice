# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 23:09:45 2021

@author: Farzana Eva
"""

"""
PROBLEM STATEMENT:
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
Example:
Given s = "Hello World",
return 5 as length("World") = 5.
Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.
"""

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        count = 0
        for i in range(len(A)-1, -1, -1):
            if i < len(A)-1:
                if A[i] == ' ' and A[i+1]!= ' ': 
                    break
            if A[i] == ' ': continue
            count+=1

        return count
