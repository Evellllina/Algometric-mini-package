import time
from typing import Callable, Any

def timeit_once(func: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start


def benchmark_sorts(mas: dict[str, list], algor: dict[str, Callable]) -> dict[str, dict]:#словарь, где ключ-имя массива, значение-другой словарь
    results: dict[str, dict] = {}
    for mas_name, mas_val in mas.items(): #для каждого массива получаем имя и сам массив
        results[mas_name] = {} #хранение всех результатов для этого массива
        for algo_name, algo in algor.items():
            try:
                time_taken = timeit_once(algo, mas_val.copy())  # ← ИСПРАВИЛ mas.copy() на mas_val.copy()
                results[mas_name][algo_name] = time_taken
            except Exception:
                results[mas_name][algo_name] = float('inf') #запись бесконечного времени
    return results
