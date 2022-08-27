# Напишите функцию, которая принимает на вход два вектора и рассчитывает косинусное расстояние данных векторов.

import numpy as np
from numpy.linalg import norm

A = np.array([192, 168])
B = np.array([0, 1])

cosine = np.dot(A, B)/(norm(A) * norm(B))
print(cosine)
