#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-24 04:48:17
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Given a binary tree, return the reverse level order traversal of its nodes values. (i.e, from left to right and from last level to starting level).

Problem Constraints
1 <= number of nodes <= 5 * 105
1 <= node value <= 105

Input Format
First and only argument is a pointer to the root node of the Binary Tree, A.

Output Format
Return an integer array denoting the reverse level order traversal from left to right.

Example Input
Input 1:
    3
   / \
  9  20
    /  \
   15   7
Input 2:
   1
  / \
 6   2
    /
   3

Example Output
Output 1:
 [15, 7, 9, 20, 3] 
Output 2:
 [3, 6, 2, 1]

Example Explanation
Explanation 1:
 Nodes as level 3 : [15, 7]
 Nodes at level 2: [9, 20]
 Nodes at level 1: [3]
 Reverse level order traversal will be: [15, 7, 9, 20, 3]
Explanation 2:
 Nodes as level 3 : [3]
 Nodes at level 2: [6, 2]
 Nodes at level 1: [1]
 Reverse level order traversal will be: [3, 6, 2, 1]
 """

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        if not A: return []

        tree_level = []

        que = deque()
        que.append(A)

        while que:
            level = []
            for i in range(len(que)):
                node = que.popleft()
                if node:
                    level.append(node.val)
                    if node.left: que.append(node.left)
                    if node.right: que.append(node.right)

            if level: tree_level.append(level)

        return [x for i in range(len(tree_level)-1, -1, -1) for x in tree_level[i]]
