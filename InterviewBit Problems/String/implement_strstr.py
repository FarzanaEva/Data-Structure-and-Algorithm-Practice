# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 02:47:30 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Another question which belongs to the category of questions which are intentionally stated vaguely. 
Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.
Implement strStr().
strstr - locate a substring ( needle ) in a string ( haystack ).
Try not to use standard library string functions for this question.
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
NOTE:
Good clarification questions:
What should be the return value if the needle is empty?
What if both haystack and needle are empty?
For the purpose of this problem, assume that the return value should be -1 in both cases.
"""
def strStr(A, B):
    if A==B: return 0
    for i in range((len(A)-len(B))):
        k = i
        for j in range(len(B)):
            if A[k] == B[j]:
                k+=1
            else: break
        if k-i == len(B): return i  
    return -1

print(strStr("b", "b"))