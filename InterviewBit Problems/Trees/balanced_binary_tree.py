#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-25 22:14:46
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a binary tree, determine if it is height-balanced.
Height-balanced binary tree  : is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :
Input : 
          1
         / \
        2   3

Return : True or 1 
Input 2 : 
         3
        /
       2
      /
     1
Return : False or 0 
         Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
         Difference = 2 > 1. 
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
    def isBalanced(self, A):
        if A == None: return 1

        if self.isBalanceHeight(A) > -1: return 1

        return 0

    def isBalanceHeight(self, A):
        if A == None: return 0

        left = self.isBalanceHeight(A.left)
        right = self.isBalanceHeight(A.right)

        if left == -1 or right == -1 or abs(left-right) > 1: return -1

        return max(left, right) + 1