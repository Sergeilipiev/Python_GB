# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# 3 Задайте список из n чисел последовательности (1+1/n)^n выведите на экран их сумму.
# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# 5 Реализуйте алгоритм перемешивания списка(shuffle использовать нельзя, другие методы из библиотеки random - можно).

import random

# 1
strnum = input('Введите вещественное число: ')
sum = 0
for i in strnum:
    if i.isdigit():
        sum += int(i)
print(sum)

# 2
n = 4
sr = []
res = 1
for i in range(1, n + 1):
    res *= i
    sr.append(res)
print(sr)

#3
n = 7
sum = 0
for i in range(1, n+1):
    sum += (1+1/i)**i
print(round(sum, 2))
# 4
n = 10
sp = list(range(-n, n+1))
mul = 1
f = open('file.txt')
for row in f:
    mul *= sp[int(row)]
print(mul)

# 5
mylist = [1, 2, 3, 4, 5, 8, 12]
print(mylist)
mylistRes = []
for i in range(len(mylist)):
    ran = random.choice(mylist)
    mylistRes.append(ran)
    mylist.remove(ran)
mylist = mylistRes
print(mylist)
