#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-14 03:03:09
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Reverse a linked list. Do it in-place and in one-pass.
For example:
Given 1->2->3->4->5->NULL,
return 5->4->3->2->1->NULL.
"""

def reverseList(A):
    if A is None: return

    prev_node = None
    curr_node = A

    while curr_node.next:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    
    curr_node.next = prev_node
    
    A = curr_node

    return A
