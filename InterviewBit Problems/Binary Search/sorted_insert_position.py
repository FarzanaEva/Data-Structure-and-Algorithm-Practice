# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:32:04 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a sorted array A and a target value B, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

**Problem Constraints**
1 <= |A| <= 100000
1 <= B <= 109

**Input Format**
First argument is array A.
Second argument is integer B.

**Output Format**
Return an integer, the answer to the problem.

**Example Input**
Input 1:
A = [1, 3, 5, 6]
B = 5
Input 2:
A = [1, 3, 5, 6]
B = 2
**Example Output**
Output 1:
 2
Output 2:
 1
"""
def searchInsert(A, B):
    start = 0
    end = len(A)-1

    while start <= end:
        mid = (start+end)//2
        if A[mid] == B: return mid
        elif A[mid] > B: end = mid - 1
        else: start = mid+1
    
    #if mid == 0: return 0
    #if mid == len(A) - 1: return mid+1
    return start

A = [ 17, 30, 32, 69, 94, 96, 106, 118, 127, 159, 169, 170, 178, 183, 209, 238, 242, 247, 253, 261, 265, 279, 288, 302, 305, 316, 352, 357, 374, 376, 392, 402, 410, 421, 439, 442, 444, 446, 454, 458, 464, 467, 468, 498, 500, 513, 523, 541, 545, 556, 575, 608, 616, 629, 631, 635, 669, 674, 682, 686, 693, 695, 719, 733, 754, 755, 756, 778, 802, 822, 824, 828, 835, 847, 848, 862, 864, 878, 883, 885, 904, 908, 928, 934 ]
print(searchInsert(A, 104))