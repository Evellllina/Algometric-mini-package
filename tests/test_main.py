import pytest
from src.algorithms import (
    factorial, fib, bubble_sort, quick_sort, counting_sort, heap_sort
)
from src.data_structures import Stack, Queue
from src.generators import (
    rand_int_array, nearly_sorted, reverse_sorted, many_duplicates
)

def test_factorial()-> None:
    assert factorial(5) == 120

def test_factorial_zero()-> None:
    assert factorial(0) == 1

def test_factorial_minus_one()-> None:
    with pytest.raises(ValueError):
        factorial(-1)

def test_fibonacci()-> None:
    assert fib(5) == 5

def test_fibonacci_zero()-> None:
    assert fib(0) == 0

def test_fibonacci_minus_one()-> None:
    with pytest.raises(ValueError):
        fib(-1)
def test_bubble_sort()-> None:
    assert bubble_sort([7, 2, 3]) == [2, 3, 7]

def test_bubble_sort_pusto()-> None:
    assert bubble_sort([]) == []

def test_bubble_sort_number()-> None:
    assert bubble_sort([5]) == [5]

def test_quick_sort()-> None:
    assert quick_sort([5, 1, 2]) == [1, 2, 5]

def test_quick_sort_pusto()-> None:
    assert quick_sort([]) == []

def test_quick_sort_number()-> None:
    assert quick_sort([4]) == [4]

def test_counting_sort()-> None:
    assert counting_sort([23, 11, 20]) == [11, 20, 23]

def test_counting_sort_pusto()-> None:
    assert counting_sort([]) == []

def test_counting_sort_number()-> None:
    assert counting_sort([100]) == [100]

def test_heap_sort()-> None:
    assert heap_sort([21, 1, 2]) == [1, 2, 21]

def test_heap_sort_pusto()-> None:
    assert heap_sort([]) == []

def test_heap_sort_number()-> None:
    assert heap_sort([57]) == [57]

def test_stack()-> None:
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.peek() == 1
    assert len(s) == 1

def test_stack_pusto()-> None:
    with pytest.raises(ValueError):
        Stack().pop()

def test_queue()-> None:
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.front() == 2
    assert len(q) == 1

def test_queue_pusto()-> None:
    with pytest.raises(ValueError):
        Queue().dequeue()

def test_rand_int_array()-> None:
    a = rand_int_array(5, 3, 15, seed=100)
    assert len(a) == 5
    assert all(3 <= x <= 15 for x in a)

def test_rand_int_array_dictinct()-> None:
    with pytest.raises(ValueError):
        rand_int_array(10, 1, 5, distinct=True)

def test_nearly_sorted()-> None:
    a = nearly_sorted(5, 2, seed=421)
    assert len(a) == 5

def test_reverse_sorted()-> None:
    assert reverse_sorted(5) == [4, 3, 2, 1, 0]

def test_many_duplicates()-> None:
    a = many_duplicates(10, 5, seed=421)
    assert len(a) == 10
    assert len(set(a)) <= 5
