class ValueNotFoundError(Exception):
    """Exception raised when a value is not found in the linked list."""
    def __init__(self, value):
        self.value = value
        self.message = f"Value '{value}' not found in the linked list."
        super().__init__(self.message)