from node_single import Node
from typing import Optional
from errors import ValueNotFoundError

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def length(self):
        return self.size

    def append(self, value: int):
        node = Node(value, None)
        if self.is_empty():
            self.head = self.tail = node
            self.head.next = self.tail
        else:
            if self.tail is not None:
                self.tail.next = node
            self.tail = node
        self.size += 1

    def prepend(self, value: int):
        node = Node(value, self.head)
        if self.is_empty():
            self.head = self.tail = node
            self.head.next = self.tail
        else:
            self.head = node
        self.size += 1

    def find(self, value: int):
        if self.is_empty():
            print("List is empty.")
            return None
        cur_node = self.head
        while (cur_node):
            if cur_node.value == value:
                return cur_node
            cur_node = cur_node.next
        print(f"Value {value} not found.")
        return None