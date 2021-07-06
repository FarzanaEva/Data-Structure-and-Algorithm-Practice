# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 04:14:51 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given an integer A, return the number of trailing zeroes in A!.
Note: Your solution should be in logarithmic time complexity.

**Problem Constraints**
1 <= A <= 10000

**Input Format**
First and only argumment is integer A.

**Output Format**
Return an integer, the answer to the problem.

**Example Input**
Input 1:
 A = 4
Input 2:
 A = 5

**Example Output**
Output 1:
 0
Output 2:
 1
**Example Explanation**
Explanation 1:

 4! = 24
Explanation 2:

 5! = 120
"""
def trailingZeroes(A):
    count = 0
    while A >= 5:
        A = A//5
        count += A

    return count




