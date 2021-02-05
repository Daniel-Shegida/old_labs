# import simple_iteration_method as simp :P
import functions_from_lab5 as funs
import matplotlib.pyplot as plt


def iteration_method_4_param(x1, eps, a, b, c, d, max):
    x2 = funs.phi_4_param(x1, a, b, c, d)
    n = 0
    while abs(x2 - x1) >= eps:
        if abs(funs.derivative_phi_4_param(x2, a, b, c)) >= 1:
            return print("Итерационный процесс расходится")
        n += 1
        x1 = x2
        x2 = funs.phi_4_param(x1, a, b, c, d)
        if n > max:
            print('ошибка')
            break
    print("Число итераций: ", n)
    print("Ответ с помощью метода простых итераций: ", x2)
    plt.scatter(x2, x2)


def iteration_method_0_param(x1, eps, max):
    x2 = funs.phi_0_param(x1)
    n = 0
    while abs(x2 - x1) >= eps:
        if abs(funs.derivative_phi_0_param(x2)) >= 1:
            return print("Итерационный процесс расходится")
        n += 1
        x1 = x2
        x2 = funs.phi_0_param(x1)
        if n > max:
            print('ошибка')
            break
    print("Число итераций: ", n)
    print("Ответ с помощью метода простых итераций: ", x2)
    plt.scatter(x2, x2)
