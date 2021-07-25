#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-25 22:35:17
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a binary search tree, write a function to find the kth smallest element in the tree.
Example :
Input : 
  2
 / \
1   3

and k = 2
Return : 2

As 2 is the second smallest element in the tree.
NOTE : You may assume 1 <= k <= Total number of nodes in BST
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
	def kthsmallest(self, A, B):
        if A == None: return
        nums = [0, 0]
        self.inOrderTraverse(A, nums, B)

        return nums[1]


    def inOrderTraverse(self, A, nums, B):
        if A == None: return

        self.inOrderTraverse(A.left, nums, B)
        nums[0]+=1
        if nums[0] == B:
            nums[1] = A.val
            return
        self.inOrderTraverse(A.right, nums, B)
