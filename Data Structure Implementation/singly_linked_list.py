#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-14 00:38:50
# @Author  : Farzana Eva 
# @Version : 1.0.0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertData(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def getLen(self):
        count = 0
        current = self.head
        while current:
            count+=1
            current = current.next
        
        return count

    def insertAt(self, data, index):
        new_node = Node(data)
        list_length = self.getLen()

        if list_length < index or index < 0: raise "index out of bound!!"

        #insert at beginning
        if index == 0:
            new_node.next = self.head
            self.head = new_node

        #insert at ending
        elif index == list_length:
            current = self.head
            while current.next:
                current = current.next
            
            current.next = new_node

        #insert at other index
        else:
            i = 0
            current = self.head
            prev = self.head
            while current.next:
                if i == index:
                    prev.next = new_node
                    new_node.next = current
                    break

                prev = current
                current = current.next
                i += 1
        
        print("{} is inserted at index position {}".format(data, index))

    def deleteAt(self, index):
        list_length = self.getLen()

        if list_length < index or index < 0: raise "index out of bound!!"

        #delete at beginning
        if index == 0:
            temp_node = self.head.next
            self.head.next = None
            self.head = temp_node

        #delete at ending
        elif index == list_length:
            current = self.head
            prev = self.head

            while current.next:
                prev = current
                current = current.next

            prev.next = None
        
        #delete at other index
        else:
            current = self.head
            prev = self.head

            i = 0
            while current.next:
                if i == index:
                    prev.next = current.next
                    current.next = None
                    break

                prev = current
                current = current.next
                i += 1

        print("data is deleted from index position {}".format(index))

    def printList(self):
        current = self.head

        while current:
            print(current.data, end = " ")
            current = current.next

        print("\n")


if __name__ == "__main__":
    llist = LinkedList()

    #create a linked list
    for i in range(5):
        llist.insertData(i)

    #print the linked list
    llist.printList()

    #get the length of linked list
    print("Length of the list is: ",llist.getLen())

    #insert at the beginning of the list
    llist.insertAt(10, 0) #insertAt(data, index)
    #insert at the ending of the list
    llist.insertAt(-1, llist.getLen())
    #insert at the ending of the list
    llist.insertAt(8, 3)

    print("After insertation: ")
    llist.printList()

    #delete at the beginning
    llist.deleteAt(0)
    #delete at the end
    llist.deleteAt(llist.getLen())
    #delete at the other index
    llist.deleteAt(2)

    print("After deletion")
    llist.printList()
