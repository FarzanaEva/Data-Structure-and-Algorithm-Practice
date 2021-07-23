#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-24 04:58:30
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a binary tree A of integers. Return an array of integers representing the right view of the Binary tree.
Right view of a Binary Tree: is a set of nodes visible when the tree is visited from Right side.

Problem Constraints
1 <= Number of nodes in binary tree <= 105
0 <= node values <= 109 

Input Format
First and only argument is an pointer to the root of binary tree A.

Output Format
Return an integer array denoting the right view of the binary tree A.

Example Input
Input 1:
        1
      /   \
     2    3
    / \  / \
   4   5 6  7
  /
 8 
Input 2:

    1
   /  \
  2    3
   \
    4
     \
      5


Example Output
Output 1:

 [1, 3, 7, 8]
Output 2:

 [1, 3, 4, 5]
 """

 # Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        if not A: return []
        que = deque() 
        right_view = []

        que.append(A)

        while que: 
            level = []
            for i in range(len(que)):
                current = que.popleft()
                if current:
                    level.append(current.val)
                    que.append(current.left)
                    que.append(current.right)

            if level: right_view.append(level[-1])
        
        return right_view
