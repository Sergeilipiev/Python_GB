
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# 1
day = int(input('введите день недели '))
if 0 < day < 6:
    print('нет')
elif 5 < day < 8:
    print('да')
else:
    print('нет такого дня недели')

#2
for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            print(x,'AND',y,'OR',z,'=',x and y or z)

#3
x, y = int(input('x:')),  int(input('y:'))
if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
else:
    print('использование 0 координат запрещено')

#4
x = int(input('Введите номер четверти: '))
if x == 1:
    print("x > 0; y > 0")
elif x == 2:
    print("x < 0; y > 0")
elif x == 3:
    print("x < 0; y < 0")
elif x == 4:
    print("x > 0; y < 0")
else:
    print('Такой четверти нету')

#5
a = input('Введите координаты точки A через запятую: ')
b = input('Введите координаты точки Б через запятую: ')
sa = a.split(',')
sb = b.split(',')
print(round(((float(sa[0]) - float(sb[0])) ** 2 + (float(sa[1]) - float(sb[1])) ** 2) ** 0.5, 2))
