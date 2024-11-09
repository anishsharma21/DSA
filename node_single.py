class Node:
    def __init__(self, value: int, next: 'Node'):
        self.value: int = value;
        self.next: Node = next;