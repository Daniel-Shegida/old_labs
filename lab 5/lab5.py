import simple_iteration_method as simp
import newton_method as new
import dichotomy_method as dic
import matplotlib.pyplot as plt
import numpy as np
import functions_from_lab5 as funs


def create_plot(x, y1, y2, title):
    plt.title(title)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.grid(True)
    plt.show()


# Вводим начальные значения
eps = float(input("Допустимая точность эпсилон: "))
max = int(input("Максимальное кол-во итераций : "))
print('x * 2^x = 1')
intervalA = float(input("Граница интервала A: "))
intervalB = float(input("Граница интервала B: "))
# выводим график для выбора начального значения х1
xnew = np.linspace(intervalA, intervalB, 1000)
ynew = [funs.fun_0_param(i) + 1 for i in xnew]
ynew1 = [1 for i in xnew]
create_plot(xnew, ynew, ynew1, "график f(x)")

x1 = float(input("Введите начальное значение х1: "))
print("\n-----------------------------------------------------------------")
print("Метод простых итераций")
simp.iteration_method_0_param(x1, eps, max)
# Показываем графики для метода простых итераций
xnew = np.linspace(intervalA, intervalB, 1000)
ynew = [funs.phi_0_param(i) for i in xnew]
create_plot(xnew, xnew, ynew, "Метод простых итераций")

print("\n-----------------------------------------------------------------")
print("Метод Ньютона")
new.newton_method_0_param(x1, eps, max)
# Показываем графики для метода Ньютона
xnew = np.linspace(intervalA, intervalB, 1000)
ynew = [funs.fun_0_param(i) + 1 for i in xnew]
ynew1 = [1 for i in xnew]
create_plot(xnew, ynew, ynew1, "метода Ньютона")

print("\n-----------------------------------------------------------------")
print("Метод дихотомии")
dic.dichotomy_method_0_param(eps, intervalA, intervalB, max)
# Показываем графики для метода дихотомии
xnew = np.linspace(intervalA, intervalB, 1000)
ynew = [funs.fun_0_param(i) + 1 for i in xnew]
ynew1 = [1 for i in xnew]
create_plot(xnew, ynew, ynew1, "Метод дихотомии")

# Вводим начальные значения
intervalA = float(input("Граница интервала A: "))
intervalB = float(input("Граница интервала B: "))
a = float(input("Введите значение a : "))
b = float(input("Введите значение b : "))
c = float(input("Введите значение c : "))
d = float(input("Введите значение d : "))

# выводим график для выбора начального значения х1
print('функция ax^3 +bx^2 + cx + d = 0')
xnew = np.linspace(intervalA, intervalB, 1000)
ynew = [funs.fun_4_param(i, a, b, c, d) for i in xnew]
ynew1 = [0 for i in xnew]
create_plot(xnew, ynew, ynew1, "график f(x)")

x1 = float(input("Введите начальное значение х1: "))
print("\n-----------------------------------------------------------------")
print("Метод простых итераций")
simp.iteration_method_4_param(x1, eps, a, b, c, d, max)
# Показываем графики для метода простых итераций
xnew = np.linspace(intervalA, intervalB, 1000)
ynew = [funs.phi_4_param(i, a, b, c, d) for i in xnew]
create_plot(xnew, xnew, ynew, "Метод простых итераций")

print("\n-----------------------------------------------------------------")
print("Метод Ньютона")
new.newton_method_4_param(x1, eps, a, b, c, d, max)
# Показываем графики для метода Ньютона
xnew = np.linspace(intervalA, intervalB, 1000)
ynew = [funs.fun_4_param(i, a, b, c, d) for i in xnew]
ynew1 = [0 for i in xnew]
create_plot(xnew, ynew, ynew1, "метода Ньютона")
print("\n-----------------------------------------------------------------")
print("Метод дихотомии")
dic.dichotomy_method_4_param(eps, intervalA, intervalB, a, b, c, d, max)
# Показываем графики для метода дихотомии
xnew = np.linspace(intervalA, intervalB, 1000)
ynew = [funs.fun_4_param(i, a, b, c, d) for i in xnew]
ynew1 = [0 for i in xnew]
create_plot(xnew, ynew, ynew1, "Метод дихотомии")
