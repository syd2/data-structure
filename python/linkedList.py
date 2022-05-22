
class Node:

    def __init__(self, data):
        self.data = data
        self.nxt = None
    
class LinkedList:

    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.nxt = self.head
        self.head = new_node
    
    def insert(self, prev, item):
        if prev is None:
            print("the previous node must be in thelinked list")
        new_node = Node(item)
        new_node.nxt = prev.nxt
        prev.nxt = new_node
    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        
        curr = self.head
        while(curr.nxt):
            curr = curr.nxt
        curr.nxt = new_node
    def print(self):
        curr = self.head
        while (curr):
            print(curr.data)
            curr = curr.nxt


l = LinkedList()
l.push(2)
l.push(3)
l.insert(l.head, 4)
l.append(5)
l.print()
