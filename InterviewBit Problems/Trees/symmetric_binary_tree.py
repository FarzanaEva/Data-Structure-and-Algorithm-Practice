#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-26 03:04:15
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
Example :

    1
   / \
  2   2
 / \ / \
3  4 4  3
The above binary tree is symmetric. 
But the following is not:

    1
   / \
  2   2
   \   \
   3    3
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
	# @return an integer
	def isSymmetric(self, A):
        if A == None: return 1

        return int(self.checkSymmetric(A.left, A.right))

    def checkSymmetric(self, left_tree, right_tree):
        if left_tree == None or right_tree == None: return int(left_tree == right_tree)

        return int(left_tree.val == right_tree.val and self.checkSymmetric(left_tree.left, right_tree.right)\
            and self.checkSymmetric(left_tree.right, right_tree.left))
