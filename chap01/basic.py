from collections.abc import Sequence
age = int(input('Enter your age un years: '))
max_heart_rate = 206.9 - (0.67 * age)
target = 0.65 * max_heart_rate
print('Your target fat-buring heart rate is', target)


def sum_number(limit: int = 10) -> int:
    s = 0
    for n in range(1, limit):
        if n % 3 == 0 or n % 5 == 0:
            s += n
    return s


print('Data: ', sum_number())

data = [7, 11]


def sumr(seq: Sequence[int]) -> int:
    if len(seq) == 0:
        return 0
    return seq[0] + sumr(seq[1:])


print('Data: ', sumr(data))

print('Data: ', sumr([]))
