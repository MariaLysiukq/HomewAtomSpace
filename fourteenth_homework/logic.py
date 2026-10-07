def add(first_number: float, second_number: float) -> float:
    """Returns the sum of two numbers."""
    return first_number + second_number

def divide(first_number: float, second_number: float) -> float:
    """Returns the division of first_number by second_number. Raises ValueError if second_number is 0 """
    if second_number == 0:
        raise ValueError("Cannot divide by zero")
    return first_number/second_number

def is_palindrome(text: str) -> bool:
    """Checks if first_number string reads the same forwards and backwards."""
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]

class Stack:
    
    def __init__(self):
        self._items = []

    def push(self, item):
        """Adds an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Removes and returns the top item from the stack. Raises IndexError if empty """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Returns the top item without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, False otherwise."""
        return len(self._items) == 0

    def __len__(self) -> int:
        """Returns the number of items in the stack"""
        return len(self._items)
