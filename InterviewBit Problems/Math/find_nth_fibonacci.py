# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 00:23:44 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT
Given an integer A you need to find the Ath fibonacci number modulo 109 + 7.
The first fibonacci number F1 = 1
The first fibonacci number F2 = 1
The nth fibonacci number Fn = Fn-1 + Fn-2 (n > 2)

Problem Constraints
1 <= A <= 109.

Input Format
First argument is an integer A.

Output Format
Return a single integer denoting Ath fibonacci number modulo 109 + 7.

Example Input
Input 1:
 A = 4
Input 2:
 A = 3
Example Output
Output 1:
 3
Output 2:
 2

Example Explanation
Explanation 1:
 F3 = F2 + F1 = 1 + 1 = 2
 F4 = F3 + F2 = 2 + 1 = 3
Explanation 2:
 F3 = F2 + F1 = 1 + 1 = 2
"""

d={}
def fibi(n):
    if(n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    elif(n==4):
        return 3
    if(n in d):
        return d[n]
    elif(n%2!=0):
        d[n]=(fibi(n//2)**2 + fibi(n//2+1)**2)%(10**9+7)
        return d[n]
    else:
        d[n]=(2*fibi(n//2)**2 + fibi(n//2-3)*fibi(n//2))%(10**9+7)
        return d[n]
    
def solve(A):
    return fibi(A)