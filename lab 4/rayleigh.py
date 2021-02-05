
import random
import numpy as np
import histogram
from dispersion import expected, varianceTheoria


def rel(s, x):
    return (x / (s ** 2)) * np.exp(-1 * ((x ** 2) / (2 * (s ** 2))))


def NeimanRel(s, n):
    x = []
    while len(x) < n:
        # пункт 3: метод Неймана
        rand1 = random.random()
        rand2 = random.random()
        Xx = 4 * s * rand1
        Y = 6 * rand2
        if Y < rel(s, Xx):
            x.append(Xx)
    return x


def MainNeimanRel(n):
    print('введите сигму')
    s = float(input())
    x = NeimanRel(s, n)
    print(x)
    print("график ")
    histogram.histogram(2, x, 0, 1.02 * max(x), 2, s)
    print("Распределение Рэлея")
    print("дисперсия и момент теоритический :")
    print("m: ", np.sqrt((np.pi * (s ** 2)) / 2))
    print("дисперсия: ", (2 - np.pi / 2) * (s ** 2))
    print("дисперсия и момент программные :")
    expected(x)
    varianceTheoria(x,np.sqrt((np.pi * (s ** 2)) / 2))
