#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-14 22:09:05
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.
For example, given following linked lists :
  5 -> 8 -> 20 
  4 -> 11 -> 15
The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20
"""

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
        head_node = ListNode(0)
        new_node = head_node

        while True:
            if A is None:
                new_node.next = B
                break
            if B is None:
                new_node.next = A 
                break
            
            if A.val<= B.val:
                new_node.next = A
                A = A.next
            else:
                new_node.next = B 
                B = B.next
            
            new_node = new_node.next
        
        return head_node.next
