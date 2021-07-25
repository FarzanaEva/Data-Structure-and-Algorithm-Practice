#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-26 02:15:24
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

NOTE : The path has to end on a leaf node.
Example :

         1
        /
       2
min depth = 2.
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def minDepth(self, A):
        if A == None: return 0

        left_depth = self.minDepth(A.left)
        right_depth = self.minDepth(A.right)

        if left_depth==0 or right_depth==0: return max(left_depth, right_depth)+1

        return min(left_depth, right_depth)+1 