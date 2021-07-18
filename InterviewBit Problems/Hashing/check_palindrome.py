#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-19 03:40:40
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a string A consisting of lowercase characters.
Check if characters of the given string can be rearranged to form a palindrome.
Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.

Problem Constraints
1 <= |A| <= 105
A consists only of lower-case characters.

Input Format
First argument is an string A.

Output Format
Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.

Example Input
Input 1:
 A = "abcde"
Input 2:
 A = "abbaee"

Example Output
Output 1:
 0
Output 2:
 1

Example Explanation
Explanation 1:
 No possible rearrangement to make the string palindrome.
Explanation 2:
 Given string "abbaee" can be rearranged to "aebbea" to form a palindrome.
 """

 class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        char_dict = {}
        odd_count = 0

        for c in A:
            if c in char_dict:
                char_dict[c] += 1
            else: char_dict[c] = 1

        for key, val in char_dict.items():
            if val % 2 == 1: odd_count += 1


        if len(A)%2 == 0 and odd_count == 0: return 1
        elif len(A)%2 == 1 and odd_count == 1: return 1

        return 0