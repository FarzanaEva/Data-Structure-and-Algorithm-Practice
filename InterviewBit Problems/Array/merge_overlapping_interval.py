# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 14:08:26 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.
"""


def merge(intervals):
    intervals.sort()
    start = intervals[0][0]
    end = intervals[0][-1]
    merged_interval = []

    for i in range(1, len(intervals)):
        if end >= intervals[i][0]:
            if end < intervals[i][-1]:
                end = intervals[i][-1]
        else:
            merged_interval.append((start, end))
            start = intervals[i][0]
            end = intervals[i][-1]
    
    if len(merged_interval) > 0:
        merged_interval.append((start, end))
    else: return (start, end)
    
    return merged_interval

print(merge([ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]))