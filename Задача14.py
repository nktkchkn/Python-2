# Задача 14: Требуется вывести все целые степени 
# двойки (т.е. числа вида 2k), не превосходящие числа N.

N = abs(int(input('Введите число N: ')))
stop = 0
a = 2
for i in range(N):
    if stop != 1:
        a = a ** i
        if a <= N:
            print(a, end=' ')
            a = 2
        else:
            stop = 1
    else:
        i = N