"""Односвязный список."""

from typing import Any, Iterator, Optional, TypeVar

T = TypeVar('T')

class Node:
    """Узел односвязного списка."""
    
    def __init__(self, data: T) -> None:
        self.data = data
        self.next: Optional['Node'] = None
    
    def __repr__(self) -> str:
        return f"Node({self.data})"

class SinglyLinkedList:
    """Односвязный список."""
    
    def __init__(self) -> None:
        self._head: Optional[Node] = None
        self._size = 0
    
    def append(self, data: Any) -> None:
        """O(n) - Добавить в конец."""
        new_node = Node(data)
        if not self._head:
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1
    
    def prepend(self, data: Any) -> None:
        """O(1) - Добавить в начало."""
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node
        self._size += 1
    
    def delete_first(self) -> Any:
        """O(1) - Удалить первый элемент."""
        if not self._head:
            raise IndexError("List is empty")
        data = self._head.data
        self._head = self._head.next
        self._size -= 1
        return data
    
    def delete_last(self) -> Any:
        """O(n) - Удалить последний элемент."""
        if not self._head:
            raise IndexError("List is empty")
        if not self._head.next:
            data = self._head.data
            self._head = None
            self._size -= 1
            return data
        
        current = self._head
        while current.next.next:
            current = current.next
        data = current.next.data
        current.next = None
        self._size -= 1
        return data
    
    def find(self, data: Any) -> bool:
        """O(n) - Поиск элемента."""
        current = self._head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def size(self) -> int:
        """O(1) - Размер списка."""
        return self._size
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def __iter__(self) -> Iterator[Any]:
        """Итерация по списку."""
        current = self._head
        while current:
            yield current.data
            current = current.next
    
    def __len__(self) -> int:
        return self.size()
    
    def __repr__(self) -> str:
        items = [str(item) for item in self]
        return f"SinglyLinkedList([{', '.join(items)}])"
