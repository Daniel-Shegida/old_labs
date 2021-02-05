import SN
import rayleigh
import reverse

READY_FOR_EXIT = False




n = float(input("Введите обьем выборки: "))
while not READY_FOR_EXIT:  # начало интерфейса
    EXIT_CODE = False
    print("выберите номер задания или нажмите s для выхода")
    print ("1 - Сформировать выборку непрерывных равно распределенных на интервале (a.b) случайных величин методом "
           "обратных функций")
    print ("2 - Сформировать выборку величин, распределенных по гауссовскому закону с параметрами𝑁(𝑚, 𝜎) на основе ЦПТ")
    print ("3 - Методом Неймана сформировать выборку величин, распределенных по релеевскому закону заданным s")
    a = input()  # цикл с предусловием
    if a != "s":
        if a.isnumeric():
            a = int(a)
            if a == 1 :
                reverse.MainReverse(n)
            elif a == 2:
                SN.MainGaus(n)
            elif a == 3 :
                rayleigh.MainNeimanRel(n)
    print("хотите ли продолжить работу y/n")
    while not EXIT_CODE:
        a = input()
        if a == "n":
            exit(0)
        elif a == "y":  # если да, то выставляем флаг на выход из этого цикла
            EXIT_CODE = True  #
        else:
            print("поддерживаются только комманды \"y\" и \"n\"")