# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 04:24:00 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a string A consisting only of lowercase characters, we need to check whether it is possible to make this string a palindrome after removing exactly one character from this.
If it is possible then return 1 else return 0.

Problem Constraints
3 <= |A| <= 105
 A[i] is always a lowercase character.

Input Format
First and only argument is an string A.

Output Format
Return 1 if it is possible to convert A to palindrome by removing exactly one character else return 0.

Example Input
Input 1:
 A = "abcba"
Input 2:
 A = "abecbea"
Example Output
Output 1:
 1
Output 2:
 0
Example Explanation
Explanation 1:
 We can remove character ācā to make string palindrome
Explanation 2:
 It is not possible to make this string palindrome just by removing one character 
"""
def solve(A):
    i = 0
    j = len(A) - 1
    miss_cnt = 0

    while i<=j:
        if A[i] == A[j]:
            i += 1
            j -= 1
        else:
            miss_cnt += 1
            if miss_cnt > 1: return 0
            if A[i]== A[j-1]: j-= 1
            elif A[i+1] == A[j]: i += 1
            else: return 0
    return 1

print(solve("jubgxwdiiidwxgbbj"))