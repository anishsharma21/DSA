from node_single import Node
from typing import Optional

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
        while cur_node:
            if cur_node.value == value:
                return cur_node
            cur_node = cur_node.next
        print(f"Value {value} not found.")
        return None

    def insert(self, value: int, index: int):
        if self.is_empty():
            print("List is empty")
            return
        if index < 0 and index + self.size < 0 or index > self.size - 1:
            raise IndexError(f"Index {index} out of bounds.")
        if index < 0:
            index += self.size

        node = Node(value, None)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            cur_node = self.head
            next_node = cur_node.next
            while (index != 0):
                index -= 1
                cur_node = next_node
                next_node = next_node.next
            cur_node.next = node
            node.next = next_node
        self.size += 1

    def delete(self, value: int):
        if self.is_empty():
            print("List is empty")
            return
        cur_node = self.head
        if cur_node.value == value:
            removed_node = self.head
            self.head = self.head.next
            return removed_node
        next_node = cur_node.next
        while (next_node):
            if next_node.value == value:
                cur_node.next = next_node.next
                return next_node
            cur_node = next_node
            next_node = next_node.next
        print("Value not found")

    def traverse(self):
        if self.is_empty():
            print("[None]")
            return
        cur_node = self.head
        while (cur_node):
            if not cur_node.next:
                print(f"{cur_node.value}")
                return
            print(f"{cur_node.value} -> ", end="")
            cur_node = cur_node.next