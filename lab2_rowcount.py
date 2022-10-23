"""Вычислить сумму знакопеременного ряда -(|х(3n)|)/(3n)!, где х-матрица ранга к
(к и матрица задаются случайным образом), n - номер слагаемого. Сумма считается вычисленной,
если точность вычислений будет не меньше t знаков после запятой. У алгоритма д.б. линейная сложность.
Операция умножения –поэлементная."""

import numpy as np
import numpy as linalg
import time


start = time.time()

#  Задание матрицы
dim = np.random.randint(4, 7)
X = np.random.randint(-10, 10, (dim, dim))
k = np.linalg.matrix_rank(X)
print(f"Сгенерированная матрица X: \n{X}\nЕе ранг k = {k}")

#  Ввод t
while True:
    try:
        t = int(input('Кол-во знаков после запятой: '))
        break
    except ValueError:
        print('Введенно некорректное значение')

# Иницилизация переменных
t = 0.1 ** t
n = dif = fact = 1
res = st = 0

#  Основной алгоритм
while abs(dif) > t:
    st += res
    res += -(np.linalg.det(np.linalg.matrix_power(X, 3 * n))) / fact
    n += 1
    fact *= (3 * n - 2) * (3 * n - 1) * 3 * n
    dif = abs(st-res)
    st = 0
    print(f'{n-1}: {res} {dif}')
print(f"Сумма знакопеременного ряда:  {res}")

finish = time.time()
print(f"Время работы программы: {finish - start} секунд")
