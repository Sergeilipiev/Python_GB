# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi
d = 0.0001
cnt = 0
while not d.is_integer():
    cnt += 1
    d *= 10
print(int(pi * 10**cnt)/10**cnt)

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = 30
sp = []
for i in range(2, n+1):
    while n % i == 0:
        sp.append(i)
        n = n/i
print(sp)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

sp = [1, 2, 1, 1, 4, 5, 4, 5, 8, 7, 5, 5, 2]
sl = []
for i in sp:
    cnt = 0
    for j in sp:
        if i == j:
            cnt += 1
    if cnt == 1:
        sl.append(i)
print(sl)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = 4
str = ''
while k != 1:
    n = random.randint(0, 100)
    str += f'{n}*x**{k} + '
    if k == 2:
        str += f'{n} = 0'
    k -= 1
with open('file2.txt', 'w') as f:
    f.write(str)


# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def get_text(name):
    with open(name) as f:
        return f.read().split(' + ')


def extract(list):
    l = []
    for i in range(len(list)):
        if i != len(list) - 1:
            tmp = list[i].split('*')
        else:
            tmp = list[i].split(' = ')
        l.append(tmp[0])
    return l


l1 = list(extract(get_text('file1.txt')))
l2 = list(extract(get_text('file2.txt')))

l3 = []
for i in range(len(l1)):
    l3.append(int(l1[i]) + int(l2[i]))


def mn(sp):
    str = ''
    k = len(sp)
    cnt = 0
    while k != 1:
        str += f'{sp[cnt]}*x**{k} + '
        if k == 2:
            str += f'{sp[cnt]} = 0'
            return str
        k -= 1
        cnt += 1


with open('final.txt', 'w') as f:
    f.write(mn(l3))
