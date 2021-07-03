# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:22:46 2021

@author: Farzana Eva
"""

def merge(arr, start, mid, end):
    temp = [0] * (end - start+ 1)
    
    i, j, k = start, mid+1, 0
    
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k +=1 
            i += 1
        else:
            temp[k] = arr[j]
            k +=1 
            j += 1
    
    while i <= mid:
        temp[k] = arr[i]
        i +=1
        k +=1
    
    while j<= end:
        temp[k] = arr[j]
        j +=1
        k +=1
        
    
    for i in range(start, end+1):
        arr[i] = temp[i - start]
    

def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, mid, end)
        
    return arr 


arr = [5, 10, 2, 1, 20]
sorted_arr = merge_sort(arr, 0, len(arr)-1)
print(sorted_arr)
