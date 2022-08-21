# Написать функцию на языке Python, аргументом которой является целочисленный массив.
# Функция должна обработать целочисленный массив и вернуть только уникальные значения для данного массива.

import random

int_list = list(range(49))
unique_values = []

for i in int_list:
    int_list[i] = random.randint(-100, 100)

unique_values = set(int_list)

print(unique_values)
print(len(unique_values))
