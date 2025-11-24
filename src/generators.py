import random

def rand_int_array(size, mini, maxi, *, distinct=False, seed=None):
    """Генерирует массив случайных целых чисел"""
    if seed is not None:
        random.seed(seed)  # делает последовательность чисел предсказуемой
    if distinct and (maxi - mini + 1) < size:
        raise ValueError("The range is too small")
    if distinct:
        return random.sample(range(mini, maxi + 1), size)
    else:
        return [random.randint(mini, maxi) for _ in range(size)]


def nearly_sorted(size, a, *, seed=None):
    """Генериует массив с перестановками"""
    if seed is not None:
        random.seed(seed)
    mas = list(range(size))
    for _ in range(a):
        i, j = random.sample(range(size), 2)
        mas[i], mas[j] = mas[j], mas[i]
    return mas

def many_duplicates(size, h=5, *, seed=None):
    """енерирует массив с большим количеством повторяющихся значений"""
    if seed is not None:
        random.seed(seed)
    uniq = [random.randint(0, 100) for _ in range(h)]
    return [random.choice(uniq) for _ in range(size)]


def reverse_sorted(size):
    """Генерирует массив, отсортированный в обратном порядке"""
    return list(range(size-1, -1, -1))


def rand_float_array(size, mini=0.0, maxi=1.0, *, seed=None):
    """Генерирует массив случайных дробных чисел"""
    if seed is not None:
        random.seed(seed)
    return [random.uniform(mini, maxi) for _ in range(size)]
