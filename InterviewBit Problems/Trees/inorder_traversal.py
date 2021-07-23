#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-24 03:38:24
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a binary tree, return the inorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [1,3,2].

Using recursion is not allowed.
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):
        inorder_list = []

        stk = []

        while True:
            if A!= None:
                stk.append(A)
                A = A.left
            else:
                if len(stk) <= 0: break
                A = stk.pop()
                inorder_list.append(A.val)
                A = A.right
        
        return inorder_list