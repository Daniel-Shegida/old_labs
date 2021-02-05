
import random
import numpy as np
import histogram
from dispersion import dispersion2, varianceTheoria, expected


def gaus (s,m,N):
    x = []
    n = 6
    N = int(N)
    for i in range(N):
        v = 0
        for i in range(0, n):
            v = v + random.random()
        el = np.sqrt(12 / n) * (v - (n / 2))
        el2 = s * el + m
        x.append(el2)
    print(x)
    return x

def MainGaus(n):
    print("введите sigma")
    s = float(input())
    print ('введите m')
    m = float(input())
    x = gaus(s,m,n)
    histogram.histogram(1, x, (1 - 0.02) * np.min(x), (1 + 0.02) * np.max(x), m, s)
    print("дисперсия и момент теоритический :")
    print(s**2, m)
    print("дисперсия и момент программные :")
    varianceTheoria(x, m)
    expected(x)