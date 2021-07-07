# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 20:31:37 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
First and only argument is string A.

Output Format
Return an integer

Example Input
Input 1:
 1
Input 2:
 28

Example Output
Output 1:
 "A"
Output 2:
 "AB"
Example Explanation
Explanation 1:

 1 -> "A"
Explanation 2:

A  -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
"""
def titleToNumber(A):
    prev = 0
    for c in A:
        prev = (prev * 26) + (ord(c) - 65) + 1

    return prev

    
    
print(titleToNumber("AAC"))
