# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 03:16:44 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a string A.
Return the string A after reversing the string word by word.
NOTE:
A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.

Input Format
The only argument given is string A.
Output Format
Return the string A after reversing the string word by word.
For Example
Input 1:
    A = "the sky is blue"
Output 1:
    "blue is sky the"

Input 2:
    A = "this is ib"
Output 2:
    "ib is this"
"""
def solve(self, A):
    words = []
    length = 0
    string = ''
    for i in A:
        length+=1
    for i in A:
        length -= 1
        if i != " ":
            string += i
        else:
            if string != '':
                words[:0] += [string]
            string = ''
        if length == 0:
            if string != '':
                words[:0] += [string]
            string = ''

    return " ".join(words)