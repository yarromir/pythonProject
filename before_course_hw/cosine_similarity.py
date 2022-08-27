# Напишите функцию, которая принимает на вход два вектора и рассчитывает косинусное расстояние данных векторов.

import numpy as np
from numpy.linalg import norm
from scipy.spatial import distance

a = np.array([192, 168])
b = np.array([0, 1])


def cosine_similarity_numpy(a, b):
    cosine_numpy = 1 - np.dot(a, b) / (norm(a) * norm(b))
    return cosine_numpy


def cosine_similarity_scipy(a, b):
    cosine_scipy = distance.cosine(a, b)
    return cosine_scipy


print(cosine_similarity_numpy(a, b))
print(cosine_similarity_scipy(a, b))
