#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-13 01:54:42
# @Author  : Farzana Eva 
# @Version : 1.0.0

"""
PROBLEM STATEMENT:
Write a function that takes an unsigned integer and returns the number of  1 bits it has.
Example:
The 32-bit integer 11 has binary representation
00000000000000000000000000001011
so the function should return 3.
Note that since Java does not have unsigned int, use long for Java
"""

def numSetBits(A):
    count = 0

    while A!= 0:
        A = A&(A-1)
        count += 1
    return count
