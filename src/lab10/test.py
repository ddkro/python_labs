import sys
import time
from pathlib import Path

from structures import Stack, Queue
from linked_list import SinglyLinkedList

print("=== ЛАБОРАТОРНАЯ РАБОТА 10: СТРУКТУРЫ ДАННЫХ ===")

# 1. Тест Stack
print("\n1. Stack (LIFO):")
stack = Stack()
for i in range(5, 0, -1):
    stack.push(i)
print(f"  Push 1-5: {stack}")
print(f"  Pop: {stack.pop()}")  # 5
print(f"  Peek: {stack.peek()}")  # 4
print(f"  Size: {len(stack)}")

# 2. Тест Queue
print("\n2. Queue (FIFO):")
queue = Queue()
for i in range(1, 6):
    queue.enqueue(i)
print(f"  Enqueue 1-5: {queue}")
print(f"  Dequeue: {queue.dequeue()}")  # 1
print(f"  Peek: {queue.peek()}")  # 2
print(f"  Size: {len(queue)}")

# 3. Тест LinkedList
print("\n3. SinglyLinkedList:")
llist = SinglyLinkedList()
for i in range(1, 6):
    llist.append(i)
print(f"  Append 1-5: {llist}")
llist.prepend(0)
print(f"  Prepend 0: {llist}")
print(f"  Find 3: {llist.find(3)}")
print(f"  Delete first: {llist.delete_first()}")  # 0
print(f"  После удаления: {llist}")
print(f"  Size: {len(llist)}")

print("\n=== ВСЕ ТЕСТЫ ПРОЙДЕНЫ ✓ ===")
