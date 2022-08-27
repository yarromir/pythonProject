# Напишите функцию, которая принимает на вход два вектора и рассчитывает косинусное расстояние данных векторов.

import numpy as np
from numpy.linalg import norm
from scipy.spatial import distance

A = np.array([192, 168])
B = np.array([0, 1])

cosine_numpy = 1 - np.dot(A, B)/(norm(A) * norm(B))
print(cosine_numpy)

cosine_scipy = distance.cosine(A, B)
print(cosine_scipy)

