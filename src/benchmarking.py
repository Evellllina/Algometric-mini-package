import time

def timeit_once(func, *args, **kwargs) -> float:
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start


def benchmark_sorts(mas: dict, algor: dict) -> dict:
    results: dict = {}
    for mas_name, mas_val in mas.items():
        results[mas_name] = {}
        for algo_name, algo in algor.items():
            try:
                time_taken = timeit_once(algo, mas_val.copy())
                results[mas_name][algo_name] = time_taken
            except Exception:
                results[mas_name][algo_name] = float('inf')
    return results
