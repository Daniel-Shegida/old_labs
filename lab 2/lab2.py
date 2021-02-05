import numpy as np
import scipy as sp
import xlrd
import matplotlib.pyplot as plt
from lagrange_polynomial import get_polynomial_lagrange
from piecewise_linear_interpolation import get_piecewice_linear_interpolation
from piecewise_parabolic_interpolation import get_piecewice_parabolic_interpolation
from python_module import get_by_scipy
from switch import switch

ACCURACY = 100

# в интерфейс было решено не вставлять просьбу вставки пути
#loc = "D:\py_table_data\pytest9.xlsx"  # путь к документу excel
loc = 'D:\py_table_data\pytest12.xlsx'  # путь к документу excel
wb = xlrd.open_workbook(loc)  # открытие excel файла
READY_FOR_EXIT = False
one = []
two = []
endx = []
endy = []


def clean_table(table):
    newtable = []
    for c in table:
        if c != '':
            newtable.append(c)
    return newtable


while not READY_FOR_EXIT:  # начало интерфейса
    EXIT_CODE = False
    print("Выберете c какими наборами данных вы хотите работать")
    print("для прекращения работы с программой, введите stop")
    a = input()  # цикл с предусловием
    while a != "stop":
        if a.isnumeric():
            a = int(a)
            try:  # проверка на существование данных в внешнем файле
                print("введите какую строчку использовать за х")
                b = int(input())
                print("введите какую строчку использовать за y")
                d = int(input())
                sheet = wb.sheet_by_index(a - 1)  # выбор таблицы
                i = int(b)  # переменная, которая нужна только для отображения легенды
                tablex = clean_table(sheet.row_values(b - 1))  # вставляем в переменную значение строки
                tabley = clean_table(sheet.row_values(d - 1))  # вставляем в переменную значение строки
                tablex = [1.0, 2.0, 2.6, 4.6, 5.0, 6.0, 7.0]
                tabley = [2.0, 4.0, 3.0, 5.0, 1.0, 4.3, 6.0]

                plt.plot(tablex, tabley, '.',  # отрисовываем оригинальные точки
                         label="оригинальные наборы данных №{i}".format(i=a))
                print("what lind of method do u want? lag,lin,par,py")
                x = input()
                # в зависимости от метода соединяем точки
                for case in switch(x):
                    if case("lag"):
                        tablex, tabley = get_polynomial_lagrange(tablex, tabley, ACCURACY)
                        plt.plot(tablex, tabley,
                                 label="данные наборов №{i} через ланграндж ".format(i=a))
                        break
                    if case("lin"):
                        tablex, tabley = get_piecewice_linear_interpolation(tablex, tabley, ACCURACY)
                        plt.plot(tablex, tabley,
                                 label="данные наборов №{i} через лин ".format(i=a))
                        break
                    if case("par"):
                        tablex, tabley = get_piecewice_parabolic_interpolation(tablex, tabley, ACCURACY)
                        plt.plot(tablex, tabley,
                                 label="данные наборов №{i} через лин ".format(i=a))
                        break
                    if case("py"):
                        tablex, tabley = get_by_scipy(tablex, tabley, ACCURACY)
                        plt.plot(tablex, tabley,
                                 label="данные наборов данных №{i} через scipy".format(i=a))
                        break
                    if case():  # default
                        print('ввели неправильный метод')

            except IndexError as err:
                print("в вашем файле нет таких наборов данных error: ", err)
        print("введите stop для вывода графика или набор данных, для добавления еще 1 значений")
        a = input()

    plt.title('task #2')  # выбор названия графика
    plt.ylim(bottom=0)  # выбор начала графика от 0 по оси y
    plt.legend(loc="lower right")  # отображение легенды
    plt.show()  # показ графика
    print("хотите ли продолжить работу y/n")
    while not EXIT_CODE:
        a = input()
        if a == "n":
            exit(0)
        elif a == "y":  # если да, то выставляем флаг на выход из этого цикла
            EXIT_CODE = True  #
        else:
            print("поддерживаются только комманды \"y\" и \"n\"")

# one, two = get_piecewice_parabolic_interpolation(tablex, tabley, ACCURACY)
# tablex, tabley = get_piecewice_parabolic_interpolation2(tablex, tabley, ACCURACY)
# endx = one + tablex
# endy = two + tabley
# print(endx, endy)
# fp, residuals, rank, sv, rcond = np.polyfit(endx, endy, 2, full=True)
# # получаем  функцию-полином
# f = sp.poly1d(fp)
