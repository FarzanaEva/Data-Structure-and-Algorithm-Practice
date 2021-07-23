#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-23 04:12:52
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a binary tree, return the preorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [1,2,3].

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
	def preorderTraversal(self, A):
        if A == None: return

        stk = []
        stk.append(A)

        preorder_list = []

        while len(stk) > 0:
            A = stk.pop()
            preorder_list.append(A.val)

            if A.right:
                stk.append(A.right)
            
            if A.left:
                stk.append(A.left)

        return preorder_list