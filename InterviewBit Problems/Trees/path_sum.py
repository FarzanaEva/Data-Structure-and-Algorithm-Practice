#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-26 03:07:45
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Example :
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def hasPathSum(self, A, B):
        if A == None: return 0

        if A.left==None and A.right== None and B-A.val == 0: return 1

        return self.hasPathSum(A.left, B-A.val) or self.hasPathSum(A.right, B-A.val)