from src.algorithms import factorial, factorial_recursive
from src.algorithms import fib, fib_recursive
from src.algorithms import bubble_sort, quick_sort, counting_sort, radix_sort, bucket_sort, heap_sort
from src.data_structures import Stack
from src.data_structures import Queue
from src.generators import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted
from src.benchmarking import benchmark_sorts
from typing import Callable

def main():
    while True:
        print("1. Алгоритмы")
        print("2. Сортировки")
        print("3. Структуры данных")
        print("4. Бенчмаркинг")
        print("5. Выход")
        choice = input("Выберите опцию: ").strip()
        if choice == "1":
            algorithms_menu()
        elif choice == "2":
            sorting_menu()
        elif choice == "3":
            data_structures_menu()
        elif choice == "4":
            benchmark_menu()
        elif choice == "5":
            break
        else:
            print("Неверный ввод")


def algorithms_menu():
    print("1. Факториал")
    print("2. Фибоначчи")
    choice = input("Выберите алгоритм: ").strip()
    n = int(input("Введите число: "))  # Исправлено: было "Выберите опцию"

    if choice == "1":
        print(f"Факториал({n}) = {factorial(n)}")
        print(f"Факториал рекурсивный({n}) = {factorial_recursive(n)}")
    elif choice == "2":
        print(f"Фибоначчи({n}) = {fib(n)}")
        print(f"Фибоначчи рекурсивный({n}) = {fib_recursive(n)}")


def sorting_menu():
    print("1. Пузырьковая")
    print("2. Быстрая")
    print("3. Подсчетом")
    print("4. Поразрядная")
    print("5. Блочная")
    print("6. Пирамидальная")
    choice = input("Выберите опцию: ").strip()
    arr_input = input("Введите массив через пробел: ")
    try:
        arr = [float(x) for x in arr_input.split()]
        if all(x.is_integer() for x in arr):
            arr = [int(x) for x in arr]  # Преобразуем в int если все числа целые
    except ValueError:
        print("Ошибка ввода массива")
        return

    sort_functions: dict[str, Callable] = {
        '1': bubble_sort, '2': quick_sort, '3': counting_sort,
        '4': radix_sort, '5': bucket_sort, '6': heap_sort
    }
    if choice in sort_functions:
        sorted_arr = sort_functions[choice](arr)
        print(f"Исходный: {arr}")
        print(f"Отсортированный: {sorted_arr}")


def data_structures_menu():
    print("1. Стек")
    print("2. Очередь")
    choice = input("Выберите опцию: ").strip()
    if choice == "1":
        stack = Stack()
        while True:
            print(f"\nСтек: {stack._items}")
            print("1. Push")
            print("2. Pop")
            print("3. Peek")
            print("4. Назад")
            op = input("Операция: ").strip()
            if op == "1":
                val = int(input("Значение: "))
                stack.push(val)
            elif op == "2":
                try:
                    print(f"Pop: {stack.pop()}")
                except IndexError as e:
                    print(f"Ошибка: {e}")
            elif op == "3":
                try:
                    print(f"Peek: {stack.peek()}")
                except IndexError as e:
                    print(f"Ошибка: {e}")
            elif op == "4":
                break

    elif choice == "2":
        queue = Queue()
        while True:
            print(f"\nОчередь: {queue._items}")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Front")
            print("4. Назад")
            op = input("Операция: ").strip()
            if op == "1":
                val = int(input("Значение: "))
                queue.enqueue(val)
            elif op == "2":
                try:
                    print(f"Dequeue: {queue.dequeue()}")
                except IndexError as e:
                    print(f"Ошибка: {e}")
            elif op == "3":
                try:
                    print(f"Front: {queue.front()}")
                except IndexError as e:
                    print(f"Ошибка: {e}")
            elif op == "4":
                break


def benchmark_menu():
    try:
        size = int(input("Введите размер тестовых массивов: "))
    except ValueError:
        print("Неверный размер!")
        return
    print("\nТипы массивов:")
    print("1. Случайный 2. Почти отсортированный 3. С дубликатами 4. Обратный 5. Все")
    array_input = input("Номера через пробел: ").strip()
    array_choices = array_input.split() if array_input else []

    arrays = {}
    if '5' in array_choices or not array_choices:
        arrays = {
            f"Случайный ({size})": rand_int_array(size, 0, 100),
            f"Почти отсортированный ({size})": nearly_sorted(size, size // 10),
            f"Много дублей ({size})": many_duplicates(size, 5),
            f"Обратный ({size})": reverse_sorted(size),
        }
    else:
        valid_choices = ['1', '2', '3', '4']
        for choice in array_choices:
            if choice in valid_choices:
                if choice == '1':
                    arrays[f"Случайный ({size})"] = rand_int_array(size, 0, 100)
                elif choice == '2':
                    arrays[f"Почти отсортированный ({size})"] = nearly_sorted(size, size // 10)
                elif choice == '3':
                    arrays[f"Много дублей ({size})"] = many_duplicates(size, 5)
                elif choice == '4':
                    arrays[f"Обратный ({size})"] = reverse_sorted(size)
    print("\nАлгоритмы:")
    print("1. Пузырьковая")
    print("2. Быстрая")
    print("3. Подсчетом")
    print("4. Поразрядная")
    print("5. Блочная")
    print("6. Пирамидальная")
    print("7. Все")
    algo_input = input("Номера через пробел: ").strip()
    algo_choices = algo_input.split() if algo_input else []

    algos: dict[str, Callable[[list], list]] = {}
    if '7' in algo_choices or not algo_choices:
        algos = {
            "Пузырьковая": bubble_sort, "Быстрая": quick_sort,
            "Подсчетом": counting_sort, "Поразрядная": radix_sort,
            "Блочная": bucket_sort, "Пирамидальная": heap_sort,
        }
    else:
        valid_choices = ['1', '2', '3', '4', '5', '6']
        for choice in algo_choices:
            if choice in valid_choices:
                if choice == '1':
                    algos["Пузырьковая"] = bubble_sort
                elif choice == '2':
                    algos["Быстрая"] = quick_sort
                elif choice == '3':
                    algos["Подсчетом"] = counting_sort
                elif choice == '4':
                    algos["Поразрядная"] = radix_sort
                elif choice == '5':
                    algos["Блочная"] = bucket_sort
                elif choice == '6':
                    algos["Пирамидальная"] = heap_sort
    if not arrays:
        print("Не выбрано ни одного типа массива")
        return
    if not algos:
        print("Не выбрано ни одного алгоритма")
        return
    print(f"\nТест: {len(arrays)} массивов × {len(algos)} алгоритмов")
    print("1. Старт 2. Отмена")
    confirm = input("Выбор: ").strip()
    if confirm == '1':
        try:
            results = benchmark_sorts(arrays, algos)
            print("Результат:")
            for arr_name, times in results.items():
                print(f"\n{arr_name}:")
                for algo, t in times.items():
                    print(f"  {algo}: {t:.6f} сек")
        except Exception as e:
            print(f"Ошибка при выполнении бенчмарка: {e}")
    else:
        print("Отменен")


if __name__ == "__main__":
    main()
