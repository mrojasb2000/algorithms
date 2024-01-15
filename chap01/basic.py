from collections.abc import Sequence, Callable

def until(limit: int, 
           filter_func: Callable[[int], bool],
           v: int) -> list[int]:
    if v == limit:
        return []
    elif filter_func(v):
        return [v] + until(limit, filter_func, v + 1)
    else:
        return until(limit, filter_func, v + 1)

def sumr(seq: Sequence[int]) -> int:
    if len(seq) == 0:
        return 0
    return seq[0] + sumr(seq[1:])

def mul_3_5(x: int) -> bool:
    return x % 3 == 0 or x % 5 == 0

def sum_functional(limit: int = 10) -> int:
    return sumr(until(limit, mul_3_5, 0))

print(until(10, mul_3_5, 0))

print(sum_functional())