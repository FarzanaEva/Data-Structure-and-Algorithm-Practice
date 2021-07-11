# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 02:09:52 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given two sorted integer arrays A and B, merge B into A as one sorted array.
Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
TIP: C users, please malloc the result into a new array and return the result.
If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after your code is executed should be m + n
Example :
Input : 
         A : [1 5 8]
         B : [6 9]

Modified A : [1 5 6 8 9]
"""
def merge(A, B):
    temp = [0] * (len(A)+len(B))

    i = 0
    j = 0
    k = 0
    while i<len(A) and j<len(B):
        if A[i] < B[j]:
            temp[k] = A[i]
            i+=1
            k+=1
        else:
            temp[k] = B[j]
            j+=1
            k+=1

    for l in range(i, len(A)):
        temp[k] = A[l]
        k+=1
    
    for r in range(j, len(B)):
        temp[k] = B[r]
        k+=1

    A += [0]*len(B)

    for i in range(len(temp)):
        A[i] = temp[i]

    return A


A = [1, 1, 1, 1, 2, 7, 9]
B = [0, 3, 5, 7, 10]

print(merge(A, B))