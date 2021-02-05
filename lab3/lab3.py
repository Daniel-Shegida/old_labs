import numpy as np
import scipy as sp
import xlrd
import matplotlib.pyplot as plt

ACCURACY = 100

# в интерфейс было решено не вставлять просьбу вставки пути
#loc = "D:\py_table_data\pytest8.xlsx"  # путь к документу excel
loc = "D:\py_table_data\pytest17y" \
      ".xlsx"  # путь к документу excel
wb = xlrd.open_workbook(loc)  # открытие excel файла
READY_FOR_EXIT = False




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
                tablex = (sheet.row_values(b - 1))  # вставляем в переменную значение строки
                tabley = (sheet.row_values(d - 1))  # вставляем в переменную значение строки
                print(tablex,tabley)
                plt.plot(tablex, tabley, '.',  # отрисовываем оригинальные точки
                         label="оригинальные наборы данных №{i}".format(i=a))
                print("введите с полиномом в какой степени вы хотите работать")
                power = int(input())
                # получаем параметры модели для полинома степени power
                fp = np.polyfit(tablex, tabley, power)
                # получаем  функцию-полином
                f = sp.poly1d(fp)
                # соединяем точки в зависимости от нашей системы
                xnew = np.linspace(np.min(tablex), np.max(tablex),ACCURACY)
                ynew = f(xnew)
                plt.plot(xnew, f(ynew), label="наборы данных №{i} c полиномом в степени {d}".format(i=a, d=power))
                print("введите stop для вывода графика или набор данных, для добавления еще 1 значений")
            except IndexError as err:
                print("в вашем файле нет таких наборов данных error: ", err)
        a = input()

    plt.title('task #3')  # выбор названия графика
    plt.ylim(bottom=0)  # выбор начала графика от 0 по оси y
    plt.legend(loc="lower right")  # отображение легенды
    axes = plt.gca()
    axes.set_ylim([0, 10])
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

# def polynomial(x, coef):
#     n = len(coef)
#     s = 0
#     for i in range(0,n):
#         s = s*x+coef[i]
#     return s
#
# cf = [1,2,3,4,5]
# # 2^4+2*2^3+3*2^2+4*2+5
# print(polynomial(2,cf))