"""Базовые структуры данных: Stack и Queue."""

from typing import Any, Iterator, TypeVar
from collections import deque

T = TypeVar('T')

class Stack:
    """Стек LIFO (Last In, First Out) на базе list."""
    
    def __init__(self) -> None:
        self._items: list[Any] = []
    
    def push(self, item: Any) -> None:
        """O(1) - Добавить элемент на вершину."""
        self._items.append(item)
    
    def pop(self) -> Any:
        """O(1) - Удалить и вернуть элемент с вершины."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()
    
    def peek(self) -> Any:
        """O(1) - Посмотреть вершину без удаления."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """O(1) - Пуст ли стек."""
        return len(self._items) == 0
    
    def size(self) -> int:
        """O(1) - Размер стека."""
        return len(self._items)
    
    def __iter__(self) -> Iterator[Any]:
        """Итерация снизу вверх."""
        return iter(self._items)
    
    def __len__(self) -> int:
        return self.size()
    
    def __repr__(self) -> str:
        return f"Stack({self._items})"

class Queue:
    """Очередь FIFO (First In, First Out) на базе deque."""
    
    def __init__(self) -> None:
        self._items: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None:
        """O(1) - Добавить в конец очереди."""
        self._items.append(item)
    
    def dequeue(self) -> Any:
        """O(1) - Удалить и вернуть с начала очереди."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items.popleft()
    
    def peek(self) -> Any:
        """O(1) - Посмотреть начало без удаления."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items[0]
    
    def is_empty(self) -> bool:
        """O(1) - Пуст ли очередь."""
        return len(self._items) == 0
    
    def size(self) -> int:
        """O(1) - Размер очереди."""
        return len(self._items)
    
    def __iter__(self) -> Iterator[Any]:
        """Итерация слева направо."""
        return iter(self._items)
    
    def __len__(self) -> int:
        return self.size()
    
    def __repr__(self) -> str:
        return f"Queue({list(self._items)})"
