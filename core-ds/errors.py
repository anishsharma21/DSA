class NodeNotFoundError(Exception):
    """Exception raised when a node is not found"""
    def __init__(self, value: str | None = "undefined"):
        self.value = value
        self.message = f"Node {value} not found in the linked list."
        super().__init__(self.message)