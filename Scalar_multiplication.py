# Напишите функцию, которая на вход принимает два вектора (два одномерных массива) и
# возвращает скалярное произведение данных векторов.

import numpy as np

a = [2, 4]
b = [3, 7]
s = 0


def scalar_multiplication(a, b):
    s = np.dot(a, b)


print(scalar_multiplication(a, b))
