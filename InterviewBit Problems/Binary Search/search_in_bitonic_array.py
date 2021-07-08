# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 02:28:37 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.
NOTE:
A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.
Problem Constraints
3 <= N <= 105
1 <= A[i], B <= 108
Given array always contain a bitonic point.
Array A always contain distinct elements.

Input Format
First argument is an integer array A denoting the bitonic sequence.
Second argument is an integer B.

Output Format
Return a single integer denoting the position (0 index based) of the element B in the array A if B doesn't exist in A return -1.

Example Input
Input 1:
 A = [3, 9, 10, 20, 17, 5, 1]
 B = 20
Input 2:
 A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
 B = 30

Example Output
Output 1:
 3
Output 2:
 -1

Example Explanation
Explanation 1:

 B = 20 present in A at index 3
Explanation 2:

 B = 30 is not present in A
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        mid = self.get_peak_point(A)
        indx = self.binary_search(A[:mid+1], B)
        if indx != -1: return indx
        indx = self.binary_search(A[:mid:-1], B)
        if indx !=-1: return mid+(len(A[mid+1:]) - indx)
        return -1

    def get_peak_point(self, A):
        start = 0
        end = len(A) - 1

        while start <= end:
            mid = start + (end -start)//2

            if (mid > 0 and mid < len(A) - 1):
                if (A[mid - 1] < A[mid] and A[mid] > A[mid+1]):
                    return mid
                elif (A[mid - 1] < A[mid] and A[mid] < A[mid+1]):
                    start = mid + 1
                else: end = mid - 1

    
    def binary_search(self, A, B):
        start = 0
        end = len(A)-1

        while start <= end:
            mid = (start+end)//2
            if A[mid] == B: return mid
            elif A[mid] > B: end = mid - 1
            else: start = mid+1
        return -1
    
A = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11 ]
B = 12
print(Solution().solve(A, B))