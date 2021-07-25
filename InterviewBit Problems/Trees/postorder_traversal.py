#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-25 23:24:07
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a binary tree, return the postorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [3,2,1].

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
	def postorderTraversal(self, A):
        postorder_list = []

        stk = []
        current = A 

        while current!= None or len(stk) > 0:
            if current != None:
                stk.append(current)
                current = current.left
            else:
                temp = stk[-1].right

                if temp == None:
                    temp = stk.pop()
                    postorder_list.append(temp.val)
                    while len(stk) > 0 and temp == stk[-1].right:
                        temp = stk.pop()
                        postorder_list.append(temp.val)

                else: current = temp

        return postorder_list
