#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-14 03:30:37
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

begin to intersect at node c1.

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        
        A_len = self.getLen(A)
        B_len = self.getLen(B)

        A_current = A
        B_current = B 

        if A_len - B_len > 0:
            for i in range(abs(A_len-B_len)):
                A_current = A_current.next
        else:
            for i in range(abs(A_len-B_len)):
                B_current = B_current.next

        while A_current and B_current:
            if A_current == B_current:
                return A_current

            A_current = A_current.next
            B_current = B_current.next

        return 

    def getLen(self, L):
        count = 0
        current = L
        while current:
            count+=1
            current = current.next
        
        return count
