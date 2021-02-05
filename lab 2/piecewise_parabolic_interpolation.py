import numpy as np

from bubble import bubble_sort


def piecewice_parabolic_interpolation(f_x, f_y, arg):
    for i in range(len(f_x) - 1):
        if f_x[i + 1] >= arg >= f_x[i]:
            if i == len(f_x) - 2:
                print("s", arg, i, f_x[i + 1])
                y0 = f_y[i - 1]
                y1 = f_y[i]
                y2 = f_y[i + 1]
                x0 = f_x[i - 1]
                x1 = f_x[i]
                x2 = f_x[i + 1]
                return y0 + (y1 - y0) * (arg - x0) / (x1 - x0) + (1 / (x2 - x0)) * (arg - x0) * (arg - x1) * (
                        ((y2 - y1) / (x2 - x1)) - ((y1 - y0) / (x1 - x0)))
            else:
                y0 = f_y[i]
                y1 = f_y[i + 1]
                y2 = f_y[i + 2]
                x0 = f_x[i]
                x1 = f_x[i + 1]
                x2 = f_x[i + 2]
                return y0 + (y1 - y0) * (arg - x0) / (x1 - x0) + (1 / (x2 - x0)) * (arg - x0) * (arg - x1) * (
                        ((y2 - y1) / (x2 - x1)) - ((y1 - y0) / (x1 - x0)))


def get_piecewice_parabolic_interpolation(x, y, z):
    print("сортировка массивов")
    print(x, y)
    bubble_sort(x, y)
    print(x, y)
    xnew = np.linspace(np.min(x), np.max(x), z)
    ynew = [piecewice_parabolic_interpolation(x, y, i) for i in xnew]
    return xnew, ynew

# #x = np.array([2, 5, -6, 7, 4, 3, 8, 9, 1, -2], dtype=float)
# x = np.array([-6, -2, 1, 2, 3, 4, 5, 7,   8, 9], dtype=float)
# y = np.array([-1, 77, -297, 249, 33, 9, 389, 573, -3, -21], dtype=float)
# xnew = np.linspace(np.min(x), np.max(x), 100)
# ynew = [piecewice_parabolic_interpolation(x, y, i) for i in xnew]
# print(ynew)
# plt.plot(x, y, 'o', xnew, ynew)
# plt.grid(True)
#
# plt.show()


# def get_piecewice_parabolic_interpolation2(x, y, z):
#     print("сортировка массивов")
#     print(x, y)
#     bubble_sort(x, y)
#     print(x, y)
#     xnew = np.linspace(np.min(x), np.max(x), z)
#     ynew = [piecewice_parabolic_interpolation2(x, y, i) for i in xnew]
#     return xnew, ynew
#
#
# def piecewice_parabolic_interpolation2(f_x, f_y, arg):
#     for i in range(len(f_x) - 1):
#         if (arg <= f_x[i + 1] and arg >= f_x[i]):
#             if i == 1  :
#                 print("s",arg, i, f_x[i + 1] )
#                 y0 = f_y[i]
#                 y1 = f_y[i + 1]
#                 y2 = f_y[i + 2]
#                 x0 = f_x[i]
#                 x1 = f_x[i + 1]
#                 x2 = f_x[i + 2]
#                 return y0 + (y1 - y0) * (arg - x0) / (x1 - x0) + (1 / (x2 - x0)) * (arg - x0) * (arg - x1) * (
#                         ((y2 - y1) / (x2 - x1)) - ((y1 - y0) / (x1 - x0)));
#             else :
#                 y0 = f_y[i - 1]
#                 y1 = f_y[i]
#                 y2 = f_y[i + 1]
#                 x0 = f_x[i - 1]
#                 x1 = f_x[i]
#                 x2 = f_x[i + 1]
#                 return y0 + (y1 - y0) * (arg - x0) / (x1 - x0) + (1 / (x2 - x0)) * (arg - x0) * (arg - x1) * (
#                             ((y2 - y1) / (x2 - x1)) - ((y1 - y0) / (x1 - x0)));
