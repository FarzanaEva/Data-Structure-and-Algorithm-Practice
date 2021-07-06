# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 04:13:21 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a number N, find all prime numbers upto N ( N included ).

Example:

if N = 7,
all primes till 7 = {2, 3, 5, 7}
Make sure the returned array is sorted.
"""

def sieve(A):
    isPrime = [1]*(A+1)
    isPrime[0], isPrime[1] = 0, 0
    prime = []

    for i in range(2, A+1):
        for j in range (2, int(i**0.5)+1):
            if i%j == 0:
                isPrime[i] = 0
                break

    for i in range(2,len(isPrime)):
        if isPrime[i]:
            prime.append(i)

    return prime