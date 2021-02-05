import functions_from_lab5 as funs
import matplotlib.pyplot as plt


def newton_method_4_param(x1,eps,a,b,c,d, max):
    # dF = funs.derivative_fun_4_param(x1, a, b, c)
    # print(dF ,x1,a,b,c)
    x2 = x1 - (funs.fun_4_param(x1,a,b,c,d) / funs.derivative_fun_4_param(x1,a,b,c))
    n = 0
    while abs(x2 - x1) >= eps:
        x1 = x2
        # dF = funs.derivative_fun_4_param(x1,a,b,c)
        # if dF == 0:
        #     print("производная = 0")
        #     return 0
        x2 = x1 - (funs.fun_4_param(x1,a,b,c,d) / funs.derivative_fun_4_param(x1,a,b,c))
        n = n + 1
        if n > max:
            print('ошибка')
            break
    print("Число итераций: ", n)
    print("Ответ с помощью метода Ньютона: ", x2)
    plt.scatter(x2, 0)


def newton_method_0_param(x1, eps, max):
    x2 = x1 - (funs.fun_0_param(x1) / funs.derivative_fun_0_param(x1))
    n = 0
    while abs(x2 - x1) >= eps:
        x1 = x2
        x2 = x1 - (funs.fun_0_param(x1) / funs.derivative_fun_0_param(x1))
        n = n + 1
        if n > max:
            print('ошибка')
            break
    print("Число итераций: ", n)
    print("Ответ с помощью метода Ньютона: ", x2)
    plt.scatter(x2, 1)

