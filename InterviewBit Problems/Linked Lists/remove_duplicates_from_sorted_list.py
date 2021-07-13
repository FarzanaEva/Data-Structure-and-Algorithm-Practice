#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-14 03:59:21
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a sorted linked list, delete all duplicates such that each element appear only once.
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
        if A == None: return
        
        current = A

        next_node = current.next

        while current:
            next_node = current.next
            while next_node and current.val == next_node.val:
                next_node = next_node.next
            
            current.next = next_node
            current = current.next

        return A
