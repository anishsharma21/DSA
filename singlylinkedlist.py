from node_single import Node

class LinkedList:
    def __init__(self):
        self.head: Node
        self.tail: Node
        self.length = 0
    
    def is_empty(self):
        return self.length == 0
    
    def size(self):
        return self.length