# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 19:17:24 2021

@author: Farzana
"""

"""
PROBLEM STATEMENT:
Given a non-negative number represented as an array of digits,
add 1 to the number ( increment the number represented by the digits ).
The digits are stored such that the most significant digit is at the head of the list.

Example:
If the vector has [1, 2, 3]
the returned vector should be [1, 2, 4]
as 123 + 1 = 124.

NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer.
For example, for this problem, following are some good questions to ask :
Q : Can the input have 0’s before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES

Q : Can the output have 0’s before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.
"""

def plusOne(A):
    for i in range(len(A)-1, -1, -1):
        if A[i] == 9: A[i] = 0
        else:
            A[i]+=1
            while True:
                if A[0] == 0:
                    del A[0]
                else:
                    return A
        
    A = [1] + A
    return A

print(plusOne([0, 9, 9, 9]))