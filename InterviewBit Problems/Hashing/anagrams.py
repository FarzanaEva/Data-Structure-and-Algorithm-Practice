#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-20 04:26:06
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given an array of strings, return all groups of strings that are anagrams. 
Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.

Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp'
Note:  All inputs will be in lower-case.

Example :
Input : cat dog god tca
Output : [[1, 4], [2, 3]]
cat and tca are anagrams which correspond to index 1 and 4. 
dog and god are another set of anagrams which correspond to index 2 and 3.
The indices are 1 based ( the first element has index 1 instead of index 0).
Ordering of the result : You should not change the relative ordering of the words / phrases within the group. 
Within a group containing A[i] and A[j], A[i] comes before A[j] if i < j.
"""

class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers
	def anagrams(self, A):
        anagram_dict = {}
        anagram_groups = []

        for i in range(len(A)):
            sorted_str = ''.join(sorted(A[i]))

            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(i+1)
            else: anagram_dict[sorted_str] = [i+1]

        for key, vals in anagram_dict.items():
            anagram_groups.append(vals)

        return anagram_groups