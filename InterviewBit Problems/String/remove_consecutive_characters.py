# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 02:21:42 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a string A and integer B, remove all consecutive same characters that have length exactly B.

Problem Constraints
1 <= |A| <= 100000
1 <= B <= |A|

Input Format
First Argument is string A.
Second argument is integer B.

Output Format
Return a string after doing the removals.

Example Input
Input 1:
A = "aabcd"
B = 2
Input 2:
A = "aabbccd"
B = 2

Example Output
Output 1:
 "bcd"
Output 2:
 "d"

Example Explanation
Explanation 1:
 "aa" had length 2.
Explanation 2:
 "aa", "bb" and "cc" had length of 2.
"""

def solve(A, B):
    if len(A) == 0: return ""
    char = A[0]
    start = 0
    new_A = ""
    cnt = 1

    for i in range(1, len(A)):
        if A[i] == char:
            cnt += 1
        else:
            if cnt == B:
                start = i
            else:
                new_A += A[start:i]
                
            char = A[i]
            cnt = 1
            start = i

    if i == len(A)-1 and cnt!= B: new_A+=A[-1]
    
    return new_A

print(solve("aabbccdd", 2))