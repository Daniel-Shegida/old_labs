
import matplotlib.pyplot as plt
import numpy as np
import bubble
import polygon


def histogram(point, x, a, b, m, sigma):
    N = len(x)
    # Определяется длина группировки
    d = b - a
    k = int(1 + np.log2(N))
    deltaX = d / k
    # частоты бi
    g = []
    # wx
    # wx = [a]
    gx = []
    for i in range(k):
        sum = 0
        # границы интервала
        deltaiMin = a + i*deltaX
        deltaiMax = a + (i + 1)*deltaX
        # wx.append(deltaiMax)
        gx.append((deltaiMax + deltaiMin) / 2)
        for j in range(N):
            if deltaiMin < x[j] <= deltaiMax:
                # Колличество ki элементов выборки, попавших в
                # интервал группировки deltai
                sum += 1
        # Определяется частота бi
        g.append(sum / (N * deltaX))
    # Строим гистограмму
    plt.bar(gx, g, width=deltaX, alpha=0.5)
    if point == 0:
        plt.title("Равномерное распределение")
        # строим плотность равномерного распределения
        wx_even(a, b, x)
    elif point == 1:
        plt.title("Нормальное распределение")
        # строим плотность гауссовского распределения
        wx_gauss(x, m, sigma)
    elif point == 2:
        plt.title("Распределение Рэлея")
        print(np.sort(g),'vsdasasd')
        wx_rayleigh(x, sigma)
    plt.show()
    # вызываем функцию построения ступенчатой диаграммы
    polygon.step_fun(point, a, b, deltaX, N, x, k, m, sigma)


# нахождение плотности равномерного распределения
def wx_even(a, b, wx):
    wy = []
    for i in range(len(wx)):
        wy.append((1 / (b - a)))
    bubble.bubble_sort(wx,wy)
    plt.plot(wx, wy, color='r')


# нахождение плотности гауссовского распределения
def wx_gauss(wx, m, sigma):
    wy = []
    for i in range(len(wx)):
        wy.append((1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-1 * (wx[i] - m)**2 / (2 * (sigma ** 2))))
    bubble.bubble_sort(wx, wy)
    plt.plot(wx, wy, color='r')


# нахождение плотности элеевского распределения
def wx_rayleigh(wx, sigma):
    wy = []
    for i in range(len(wx)):
        wy.append((wx[i] / (sigma ** 2)) * np.exp(-1 * ((wx[i] ** 2) / (2 * (sigma ** 2)))))
    print(wx,"неотфильтр значения ")
    print(wy)
    bubble.bubble_sort(wx,wy)
    print(wx,"отфильтр значения ")
    print(wy)
    plt.plot(wx, wy, color='r')
































# def hist(x):
#     n = 0
#     N = 1000
#     k  = 11 * math.log10(N)
#     a = min(x)
#     b = max(x)
#     d = 1.02(max(x)-min(x))
#     dX = d/k
#     di = 0
#     for i in range (1,k+1):
#         di = (a + i*dX)
#         while flag = 0:
#             if x[n]<=di :
#                 n = n + 1
#                 end[n] = end[n] + 1
#
#
#
# ######
#
# def pol(x):
#     n = 0
#     N = 1000
#     k = 11 * math.log10(N)
#     a = min(x)
#     b = max(x)
#     d = 1.02(max(x) - min(x))
#     dX = d / k
#     di = 0
#     kk = [0]
#     yy = []
#     end = []
#     for i in range(0, k ):
#         flag = 0
#         kk.append(0)
#         print(kk)
#         di = (a + i * dX)
#         yy.append(di)
#         while flag == 0:
#             if x[n] <= di:
#                 kk[i] = kk[i] + 1
#                 n +=1
#             else:
#                 flag = 1
#     print('d',kk)
#     for i in kk:
#         end.append(i/N)
#     print('end',len(end),end)
#     print ('yy',len(yy),yy)
#






