class Stack:
    def __init__(self) -> None:
        self._items: list = []
    def push(self, x) -> None:
        self._items.append(x)
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._items.pop()
    def peek(self):
        if self.is_empty():
            raise ValueError("Empty stack")
        else:
            return self._items[-1]
    def is_empty(self) -> bool:
        return len(self._items) == 0
    def __len__(self) -> int:
        return len(self._items)


class Queue:
    def __init__(self) -> None:
        self._items: list = []
    def enqueue(self, x) -> None:
        self._items.append(x)
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Empty queue")
        else:
            return self._items.pop(0)
    def front(self):
        if self.is_empty():
            raise ValueError("Empty queue")
        return self._items[0]
    def is_empty(self) -> bool:
        return len(self._items) == 0
    def __len__(self) -> int:
        return len(self._items)
