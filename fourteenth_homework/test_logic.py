import pytest
from logic import add, divide, is_palindrome, Stack

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(39483920, 0) == 39483920

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0

def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1283208320930,0)

@pytest.mark.parametrize(
    "text, expected_result",
    [("radar", True), ("level", True), ("mariia", False), ("cats", False)]
)
def test_is_palindrome(text, expected_result) -> None:
    assert is_palindrome(text) == expected_result

@pytest.fixture
def empty_stack() -> Stack:
    """Returns a new, empty Stack instance."""
    return Stack()

@pytest.fixture
def filled_stack() -> Stack:
    """Returns a Stack pre-filled with three items."""
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    return stack

def test_stack_push_pop_order(filled_stack: Stack) -> None:
    assert filled_stack.pop() == 30
    assert filled_stack.pop() == 20
    assert filled_stack.pop() == 10

def test_stack_peek(filled_stack: Stack) -> None:
    assert filled_stack.peek() == 30
    assert len(filled_stack) == 3

def test_stack_is_empty_and_len(empty_stack: Stack) -> None:
    assert empty_stack.is_empty() is True
    assert len(empty_stack) == 0
    
    empty_stack.push("Python")
    assert empty_stack.is_empty() is False
    assert len(empty_stack) == 1

def test_stack_empty_pop_peek(empty_stack: Stack) -> None:
    with pytest.raises(IndexError, match="pop from empty stack"):
        empty_stack.pop()
        
    with pytest.raises(IndexError, match="peek from empty stack"):
        empty_stack.peek()
