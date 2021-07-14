#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-15 03:11:53
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def swapPairs(self, A):
        if A == None or A.next == None: return A

        prev_node = A
        curr_node = A.next

        A = curr_node

        while True:
            next_node = curr_node.next
            curr_node.next = prev_node

            if next_node== None or next_node.next==None:
                prev_node.next = next_node
                break
            
            prev_node.next = next_node.next
            prev_node = next_node

            curr_node = prev_node.next

        return A