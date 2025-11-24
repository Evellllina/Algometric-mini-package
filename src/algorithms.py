from typing import List, Any, Optional, Callable

def factorial(n: int) -> int:
    """Факториал"""
    if n < 0:
        raise ValueError("must be non-negative") #проверка на отрицательное число
    result = 1 #вернет начальное значение
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """Рекурсивный факториал"""
    if n < 0:
        raise ValueError("must be non-negative")
    return 1 if n <= 1 else n * factorial_recursive(n - 1)


def fib(n: int) -> int:
    """Фибоначчи"""
    if n < 0:
        raise ValueError("must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_recursive(n: int) -> int:
    """Рекурсивный фибоначчи"""
    if n < 0:
        raise ValueError("must be non-negative")
    return n if n <= 1 else fib_recursive(n - 1) + fib_recursive(n - 2)


def bubble_sort(a: List[Any], key: Optional[Callable[[Any], Any]] = None,
                cmp: Optional[Callable[[Any, Any], int]] = None) -> List[Any]:
    """Пузырьковая"""
    a = a.copy()#создаем копию, чтобы не менять факториал
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):#уменьшаем область
            a_v = key(a[j]) if key else a[j]
            b_v = key(a[j + 1]) if key else a[j + 1]
            if cmp: #сравниваем
                compare = cmp(a_v, b_v)
            else:
                compare = 1 if a_v > b_v else -1 if a_v < b_v else 0
            if compare > 0: #если порядок неправильный, меняем местами
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def quick_sort(a: List[Any], key: Optional[Callable[[Any], Any]] = None,
               cmp: Optional[Callable[[Any, Any], int]] = None) -> List[Any]:
    """Быстрая сортировка"""
    if len(a) <= 1:
        return a.copy()
    pivot = a[len(a) // 2]#выбираем опорный элемент
    left = [x for x in a if _compare(x, pivot, key, cmp) < 0]
    middle = [x for x in a if _compare(x, pivot, key, cmp) == 0]
    right = [x for x in a if _compare(x, pivot, key, cmp) > 0]
    return quick_sort(left, key, cmp) + middle + quick_sort(right, key, cmp)#рекурсивно сортируем левую и правую часть


def counting_sort(a: List[Any], key: Optional[Callable[[Any], Any]] = None,
                  cmp: Optional[Callable[[Any, Any], int]] = None) -> List[Any]:
    """Подсчетом"""
    if not a:
        return []#находим диапазон значений
    max_v = max(key(x) if key else x for x in a)
    min_v = min(key(x) if key else x for x in a)
    c = [0] * (max_v - min_v + 1)#создаем массив для подсчета
    for x in a:
        v = key(x) if key else x
        c[v - min_v] += 1#подсчитываем количество кадого элемента
    result = []
    for i, g in enumerate(c):
        result.extend([min_v + i] * g)#добавляем элемент g раз
    return result


def radix_sort(a: List[Any], base: int = 10, key: Optional[Callable[[Any], Any]] = None,
               cmp: Optional[Callable[[Any, Any], int]] = None) -> List[Any]:
    """Поразрядная сортировка"""
    if not a:
        return []
    max_v = max(key(x) if key else x for x in a)
    exp = 1 #с маладшего разряда
    while max_v // exp > 0:
        b: List[List[Any]] = [[] for _ in range(base)] #верно для каждой цифры
        for x in a:
            val = key(x) if key else x
            b[(val // exp) % base].append(x)
        a = [] #собираем обратно массив
        for bucket in b:
            a.extend(bucket)
        exp *= base#к следующему разряду
    return a


def bucket_sort(a: List[Any], buckets: Optional[int] = None,
                key: Optional[Callable[[Any], Any]] = None,
                cmp: Optional[Callable[[Any, Any], int]] = None) -> List[Any]:
    """Блочная сортировка"""
    if not a:
        return []
    if buckets is None:
        buckets = len(a)
    min_v = min(key(x) if key else x for x in a)#определяем диапазон значений
    max_v = max(key(x) if key else x for x in a)
    b_range = (max_v - min_v) / buckets#размер кадого блока
    b_list: List[List[Any]] = [[] for _ in range(buckets)]#создаем блоки
    for x in a:
        val = key(x) if key else x
        index = min(int((val - min_v) / b_range), buckets - 1)
        b_list[index].append(x)
    result = []
    for bucket in b_list:#сортируем каждый блок и объединяем
        result.extend(bubble_sort(bucket, key, cmp))
    return result


def heap_sort(a: List[Any], key: Optional[Callable[[Any], Any]] = None,
              cmp: Optional[Callable[[Any, Any], int]] = None) -> List[Any]:
    """Пирамидальная"""
    def heapify(n: int, i: int) -> None:
        k = i#корень
        left = 2 * i + 1#левый
        r = 2 * i + 2#правый
        if left < n and _compare(a[left], a[k], key, cmp) > 0:#ищем наибольший
            k = left
        if r < n and _compare(a[r], a[k], key, cmp) > 0:
            k = r

        if k != i:
            a[i], a[k] = a[k], a[i]
            heapify(n, k)
    a = a.copy()
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):#извлекаем элементы из кучи
        a[i], a[0] = a[0], a[i]
        heapify(i, 0)
    return a


def _compare(a: Any, b: Any, key: Optional[Callable[[Any], Any]] = None,
             cmp: Optional[Callable[[Any, Any], int]] = None) -> int:
    """Вспомогательная функция сравнения"""
    a_v = key(a) if key else a#применяем функцию, есди есть
    b_v = key(b) if key else b
    if cmp:
        return cmp(a_v, b_v)
    else:
        return -1 if a_v < b_v else 1 if a_v > b_v else 0
