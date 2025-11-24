class Stack:
    def __init__(self)-> None:
        self._items: list[int] = []
    def push(self, x: int) -> None:
        self._items.append(x) #добавляет элемент на вершину стека
    def pop(self) -> int:
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._items.pop() #удаляет и возвращает
    def peek(self)->int:
        if self.is_empty():
            raise ValueError("Empty stack")
        else:
            return self._items[-1] #возвращает без удаления
    def is_empty(self) -> bool:
        return len(self._items) == 0 #пуст ли стек
    def __len__(self) -> int:
        return len(self._items)


class Queue:
    def __init__(self)-> None:
        self._items: list[int] = []
    def enqueue(self, x: int) -> None:
        self._items.append(x)
    def dequeue(self) -> int:
        if self.is_empty():
            raise ValueError("Empty queue")
        else:
            return self._items.pop(0)
    def front(self) -> int:
        if self.is_empty():
            raise ValueError("Empty queue")
        return self._items[0]
    def is_empty(self)->bool:
        return len(self._items) == 0
    def __len__(self) -> int:
        return len(self._items)
