# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 01:50:16 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given the array of strings A, 
you need to find the longest string S which is the prefix of ALL the strings in the array.
Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 
and S2.
For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Input Format
The only argument given is an array of strings A.
Output Format
Return longest common prefix of all strings in A.
For Example
Input 1:
    A = ["abcdefgh", "aefghijk", "abcefgh"]
Output 1:
    "a"
    Explanation 1:
        Longest common prefix of all the strings is "a".

Input 2:
    A = ["abab", "ab", "abcd"];
Output 2:
    "ab"
    Explanation 2:
        Longest common prefix of all the strings is "ab".
"""
def longestCommonPrefix(A):
    if len(A) == 1: return A[0]
    if len(A) == 0: return ""
    
    min_len = len(A[0])
    prefix = ""

    for i in range(len(A)):
        min_len = min(min_len, len(A[i]))

    for i in range(min_len):
        current = A[0][i]
        for j in range(len(A)):
            if A[j][i]!= current:
                return prefix

        prefix += current
    
    return prefix

