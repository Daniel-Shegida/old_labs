import numpy as np

from bubble import bubble_sort


def piecewice_linear_interpolation(f_x, f_y, arg):
    for i in range(len(f_x) - 1):
        if (arg <= f_x[i + 1] and arg >= f_x[i]):
            y0 = f_y[i]
            y1 = f_y[i + 1]
            x0 = f_x[i]
            x1 = f_x[i + 1]
            return y0 + (y1 - y0) * (arg - x0) / (x1 - x0)


def get_piecewice_linear_interpolation(x, y, z):
    print("сортировка массивов")
    print(x, y)
    bubble_sort(x, y)
    print(x, y)
    xnew = np.linspace(np.min(x), np.max(x), z)
    ynew = [piecewice_linear_interpolation(x, y, i) for i in xnew]
    return xnew, ynew




    # ynew = []
    # for i in xnew:
    #     a = piecewice_linear_interpolation(x, y, i)
    #     if a == None:
    #         print("wow",i,len(x))
    #         ynew
    #     else:
    #         ynew.append(a)

    # plt.plot(x, y, 'o', xnew, ynew)
    # plt.grid(True)
    #
    # plt.show()
