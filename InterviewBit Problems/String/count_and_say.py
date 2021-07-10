# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 04:31:20 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.
21 is read off as one 2, then one 1 or 1211.
Given an integer n, generate the nth sequence.
Note: The sequence of integers will be represented as a string.
Example:
if n = 2,
the sequence is 11.
"""
def countAndSay(A):
    if A == 1: return "1"
    if A == 2: return "11"
    
    seq = "11"
    new_seq = ""
    
    for _ in range(2, A):
        new_seq = ""
        char = seq[0]
        cnt = 1
        for i in range(1, len(seq)):
            if char == seq[i]:
                cnt+= 1
            else:
                new_seq+= (str(cnt)+ char)
                char = seq[i]
                cnt = 1
        new_seq+= (str(cnt)+ char)
        seq = new_seq
    
    return new_seq 

print(countAndSay(7))