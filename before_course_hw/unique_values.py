# Написать функцию на языке Python, аргументом которой является целочисленный массив.
# Функция должна обработать целочисленный массив и вернуть только уникальные значения для данного массива.

import random

a = list(range(49))
for i in a:
    a[i] = random.randint(-100, 100)


def unique_values(a):
    a = set(a)
    return a


print(unique_values(a))
print("Number of unique values: " + str(len(unique_values(a))))
