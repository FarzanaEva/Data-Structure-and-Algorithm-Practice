#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-17 04:05:00
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Reverse a linked list using recursion.
Example :
Given 1->2->3->4->5->NULL,
return 5->4->3->2->1->NULL.
"""

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def reverseList(self, A):
        if A.next == None:
            return A 
        
        head = self.reverseList(A.next)
        temp = A.next
        temp.next = A
        A.next = None

        return head
