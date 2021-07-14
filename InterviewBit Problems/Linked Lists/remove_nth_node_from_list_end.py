#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-14 21:23:07
# @Author  : Farzana Eva 
# @Version : 1.0.0


# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

"""
PROBLEM STATEMENT:
Given a linked list, remove the nth node from the end of list and return its head.
For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
If n is greater than the size of the list, remove the first node of the list.
Try doing it using constant additional space.
"""

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def removeNthFromEnd(self, A, B):
        if A==None: return

        A_len = self.getLen(A)
        indx = A_len - B

        if A_len < B or indx == 0:
            return A.next

        elif indx == A_len-1:
            current = A
            prev = None
            while current.next:
                prev = current
                current = current.next
            prev.next = None
        
        else:
            current = A
            prev = None

            i = 0
            while current.next:
                if i == indx:
                    prev.next = current.next
                    current.next = None
                    break
                
                prev = current
                current = current.next
                i += 1
        
        return A


    def getLen(self, A):
        count = 0
        current = A
        while current:
            count+=1
            current = current.next

        return count