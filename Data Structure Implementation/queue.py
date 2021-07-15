#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-16 00:22:11
# @Author  : Farzana Eva 
# @Version : 1.0.0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        if self.front == None and self.rear == None:
            return True
        return False

    def getFront(self):
        if self.front == None:
            raise "Queue is Empty!! There is no front!!"
        return self.front.data

    def enqueue(self, val):
        new_node = Node(val)

        if self.front == None and self.rear == None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.front == None:
            raise "Queue is Empty!!"
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next

    def printQueue(self):
        current = self.front

        while current:
            print(current.data, end = " ")
            current = current.next
        print()


if __name__ == "__main__":
    que = Queue()

    que.enqueue(2)
    que.enqueue(3)
    que.enqueue(4)
    que.enqueue(5)

    que.printQueue()
    que.dequeue()
    que.dequeue()
    print("Front of the queue is : ", que.getFront())
    que.printQueue()
    que.dequeue()
    que.dequeue()
    print("Is the queue empty? : ", que.isEmpty())
