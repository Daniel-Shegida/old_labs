import math


# 0 param x * 2^x = 1
def fun_0_param(x):
    return x * (2 ** x) - 1


def phi_0_param(x):
    return 2 ** (-x)


def derivative_fun_0_param(x):
    return (2 ** x) * (1 + math.log(2) * x)


def derivative_phi_0_param(x):
    return -1 * math.log(2) / (2 ** x)


# 4 param ax^3 + bx^2 + cx + d = 0
def fun_4_param(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


def phi_4_param(x, a, b, c, d):
    return - (a * x * x * x / c + b * x ** 2 / c + d / c)


def derivative_fun_4_param(x, a, b, c):
    return 3 * a * x * x + 2 * b * x + c


def derivative_phi_4_param(x, a, b, c):
    return -(3 * a * x * x / c + b * x / c)
