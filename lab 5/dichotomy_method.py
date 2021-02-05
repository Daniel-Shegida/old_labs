import functions_from_lab5 as funs
import matplotlib.pyplot as plt


def dichotomy_method_4_param(eps, intervalA, intervalB, a, b, c, d, max):
    x = (intervalB + intervalA) / 2
    n = 0
    while intervalB - intervalA >= 2 * eps:
        n += 1
        if funs.fun_4_param(x, a, b, c, d) == 0:
            break
        if funs.fun_4_param(intervalA, a, b, c, d) * funs.fun_4_param(x, a, b, c, d) < 0:
            intervalB = x
        elif funs.fun_4_param(intervalB, a, b, c, d) * funs.fun_4_param(x, a, b, c, d) < 0:
            intervalA = x
        x = (intervalB + intervalA) / 2
        if n > max:
            print('ошибка')
            break
    print("Число итераций: ", n)
    print("Без параметров: ", x)
    plt.scatter(x, 0)


def dichotomy_method_0_param(eps, intervalA, intervalB, max):
    x = (intervalB + intervalA) / 2
    n = 0
    while intervalB - intervalA >= 2 * eps:
        n += 1
        if funs.fun_0_param(x) == 0:
            break
        if funs.fun_0_param(intervalA) * funs.fun_0_param(x) < 0:
            intervalB = x
        elif funs.fun_0_param(intervalB) * funs.fun_0_param(x) < 0:
            intervalA = x
        x = (intervalB + intervalA) / 2
        if n > max:
            print('ошибка')
            break
    print("Число итераций: ", n)
    print("Без параметров: ", x)
    plt.scatter(x, 1)
