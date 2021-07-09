# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 23:15:31 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a string A of parantheses  ‘(‘ or ‘)’.
The task is to find minimum number of parentheses ‘(‘ or ‘)’ (at any positions) we must add to make the resulting parentheses string valid.
An string is valid if:
Open brackets must be closed by the corresponding closing bracket.
Open brackets must be closed in the correct order.

Problem Constraints
1 <= |A| <= 105
A[i] = '(' or A[i] = ')'

Input Format
First and only argument is an string A.

Output Format
Return a single integer denoting the minimumnumber of parentheses ‘(‘ or ‘)’ (at any positions) we must add in A to make the resulting parentheses string valid.

Example Input
Input 1:
 A = "())"
Input 2:
 A = "((("
Example Output
Output 1:
 1
Output 2:
 3
Example Explanation
Explanation 1:
 One '(' is required at beginning.
Explanation 2:

 Three ')' is required at end.
"""
def solve(A):
    left = 0
    right = 0

    for i in range(len(A)):
        if A[i] =="(": right += 1
        elif right > 0: right -= 1
        else: left += 1

    return left+right
