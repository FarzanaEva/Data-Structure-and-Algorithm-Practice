#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-15 22:32:24
# @Author  : Farzana Eva 
# @Version : 1.0.0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        new_node = Node(val)
        if self.top:
            new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top == None:
            raise "Stack is already empty!! Invalid operation!!"
        else:
            temp = self.top.next
            self.top = temp
    
    def getTop(self):
        if self.top == None: raise "Stack is empty!!"
        return self.top.data
    
    def isEmpty(self):
        if self.top: return False
        return True
    
    def printStack(self):
        current = self.top
        while current:
            print(current.data, end = " ")
            current = current.next
        print()

if __name__ == "__main__":
    stk = Stack()

    stk.push(4)
    stk.push(3)
    print("Top value of stack: ", stk.getTop())
    stk.push(2)
    stk.printStack()
    stk.pop()
    print("is the stack empty? : ", stk.isEmpty())
    stk.pop()
    stk.printStack()

