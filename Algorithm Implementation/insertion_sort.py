# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 21:50:59 2021

@author: Farzana Eva
"""

def insertion_sort(arr):
    
    for i in range(len(arr)):
        ind = i-1
        val = arr[i]
        
        while ind >= 0 and arr[ind] > val:
            arr[ind+1] = arr[ind]
            ind -=1 
        
        arr[ind+1] = val
    return arr
        
    
print(insertion_sort([5, 10, 2, 1, 20]))