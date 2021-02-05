import numpy as np
from bubble import bubble_sort


def polynomialLagrange1(x, y, arg):
    F = []
    for i in range(len(y)):
        F.append(y[i])
    for a in range(len(y) - 1):
        for b in range(a + 1, len(y)):
            F[b] = ((arg - x[a]) * F[b] - (arg - x[b]) * F[a]) / (x[b] - x[a])
    return F[len(y) - 1]


def get_polynomial_lagrange(x, y, z):
    print("сортировка массивов")
    print(x, y)
    bubble_sort(x, y)
    print(x, y)
    xnew = np.linspace(np.min(x), np.max(x), z)
    ynew = [polynomialLagrange1(x, y, i) for i in xnew]
    return xnew, ynew


# # form LAN = Пx - xi)
# #            П(xj- xi
# def polynomialLagrange(x, y, xnew):
#     ynew = []
#     # Провегаем по всем новым значениям xnew
#     for xl in xnew:
#         # Полином Лагранжа
#         L = 0
#         # Пробегаем по всем X[i]
#         for i in range(len(x)):
#             # Промежуточные значения дроби полинома
#             p1 = 1
#             p2 = 1
#             # Пробегаем по всем X[j]
#             for j in range(len(x)):
#                 # i != j по условию, так как p2 будет равен 0
#                 if i == j:
#                     continue
#                 # Вычисляем числитель и знаменатель
#                 p1 = p1 * (xl - x[j])
#                 p2 = p2 * (x[i] - x[j])
#             # Находим поленом L[i]
#             L = L + y[i] * p1 / p2
#         # Добавляем L[i] в новый массив значений y
#         ynew.append(L)
#     return ynew




# def lagranz(x, y, t):
#     z = 0
#     for j in range(len(y)):
#         p1 = 1;
#         p2 = 1
#         for i in range(len(x)):
#             if i == j:
#                 p1 = p1 * 1;
#                 p2 = p2 * 1
#             else:
#                 p1 = p1 * (t - x[i])
#                 p2 = p2 * (x[j] - x[i])
#         z = z + y[j] * p1 / p2
#     return z

# xnew = np.linspace(np.min(x), np.max(x), 100)
# ynew = [lagranz(x, y, i) for i in xnew]
# print(ynew)
# print('s', y)
# plt.plot(x, y, 'o', xnew, ynew)
# # ynew = [polynomialLagrange1(x, y, i) for i in xnew]
# print(ynew)
# plt.plot(x, y, 'o', xnew, ynew)
# plt.grid(True)
# plt.show()