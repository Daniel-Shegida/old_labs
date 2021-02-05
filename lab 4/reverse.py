
import random
import numpy as np
import matplotlib.pyplot as plt
import histogram
from dispersion import dispersion, centralMoment, neprdispersion, varianceTheoria


def even  (a,b,sum,wx):
    h =np.sum(sum) / len(sum)
    wy = []
    for i in range (len(wx)):
        wy.append((1/(b-a))+h)
    plt.plot (wx,wy,color = 'r')


def reverse(a,b,n):
    N = int(n)  # объем выборки
    y = []
    for i in range(0, N):
        x2 = a + (b-a) * random.random()
        y.append(x2)
    print('выборка:',y)
    return y

def MainReverse(n):
    print ('введите параметры а и b')
    a = float(input())
    b = float(input())
    x = reverse(a, b,n)
    histogram.histogram(0, x, a, b, 1, 1)
    print('дисперсия теоритическая :', neprdispersion(a,b))
    print('момент теоритический :', (a + b)/2)
    print('дисперсия и момент программный :')
    dispersion(x)
    varianceTheoria(x, (a + b)/2)

