# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 03:34:26 2021

@author: Farzana Eva
"""
"""
PROBLEM STATEMENT:
A hotel manager has to process N advance bookings of rooms for the next season. His hotel has C rooms. Bookings contain an arrival date and a departure date. He wants to find out whether there are enough rooms in the hotel to satisfy the demand. Write a program that solves this problem in time O(N log N) .

Input Format
First argument is an integer array A containing arrival time of booking.
Second argument is an integer array B containing departure time of booking.
Third argument is an integer C denoting the count of rooms.

Output Format
Return True if there are enough rooms for N bookings else return False.
Return 0/1 for C programs.

Example Input
Input 1:
 A = [1, 3, 5]
 B = [2, 6, 8]
 C = 1

Example Output
Output 1:
 0
 
Example Explanation
Explanation 1:
 At day = 5, there are 2 guests in the hotel. But I have only one room.    
"""


def hotel(arrive, depart, K):
    availability = []
    count = 0
    
    for i in range(len(arrive)):
        availability.append([arrive[i], 1])
        availability.append([depart[i], -1])

    availability.sort()
    
    for i in range(len(availability)):
        count += availability[i][1]
        
        if count > K: return 0
    return 1
    

A = [ 11, 24, 36, 15, 16, 23, 20, 19 ]
B = [ 14, 32, 67, 25, 21, 54, 61, 34 ]
C = 4
 
print(hotel(A, B, C))