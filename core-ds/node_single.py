from typing import Optional

class Node:
    def __init__(self, value: int, next: 'Optional[Node]'):
        self.value: int = value;
        self.next: Optional[Node] = next;