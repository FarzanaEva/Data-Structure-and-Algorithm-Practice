#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-25 23:18:58
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a binary tree, invert the binary tree and return it. 
Look at the example for more details.

Example : 
Given binary tree

     1
   /   \
  2     3
 / \   / \
4   5 6   7
invert and return

     1
   /   \
  3     2
 / \   / \
7   6 5   4
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return the root node in the tree
	def invertTree(self, A):
        if A == None: return A

        left = self.invertTree(A.left)
        right = self.invertTree(A.right)

        A.left, A.right = right, left

        return A
