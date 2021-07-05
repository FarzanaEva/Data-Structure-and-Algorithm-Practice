# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 22:57:22 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
Make sure the returned intervals are also sorted.
"""

def insert(intervals, new_interval):
    start = new_interval[0]
    end = new_interval[1]
    
    left, right = 0, 0
    
    while right < len(intervals):
        if start <= intervals[right][1]:
            if end < intervals[right][0]:
                break
            start = min(start, intervals[right][0])
            end = max(end, intervals[right][1])
        else:
            left += 1
        right += 1
        
    if start > end: start, end = end, start
        
    return intervals[:left] + [(start, end)] + intervals[right:]
    

print(insert([ (1, 2), (3, 6) ], (10, 8)))
