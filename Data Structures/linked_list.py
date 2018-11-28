"""
Linked List 
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedLIst():
    def __init__(self):
        self.head = None
    
    def insert_in_beginning(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def print_data(self):
        currentNode = self.head
        while True:
            if currentNode == None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
            


linkedList = LinkedLIst()
linkedList.insert_in_beginning(Node(3))
linkedList.insert_in_beginning(Node(6))
linkedList.insert_in_beginning(Node(10))

linkedList.print_data()