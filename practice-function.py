# name = input("Введите ваше имя: ")
# def greeting():
#     print("-----")
#     print(f"Привет {name}, добро пожаловать")
#     print("------")
#
# greeting()
#
# print(name)
#
# def f():
#     global a
#     global b
#     b, c = a, b
# def g():
#     global a
#     global b
#     c = '0'
#     a = d + c
# a = '2'
# b = '3'
# c = '5'
# d = '7'
# f()
# g()
# f()
# print(a + b + c + d)

# # Задача 1
# def print_lines(n):
#     print("-" * n)
#     print("-" * n)
#
# n = int(input("Введите количество цепей"))
# print_lines(n)

# # Задача 2
# def print_lines(n):
#     if n < 2:
#         print("Ширина не менее 2")
#     print("-" * n)
#     print("-" + " " * (n-2) + "-")
#     print("-" * n)
#
# n = int(input("Введите количество цепей"))
# print_lines(n)

# Задача 3
# def print_tringle(n):
#     for i in range(1, n + 1):
#         print("*" * i)
# n = int(input("Введите количество звезд"))
# print_tringle(n)
# Задача 7
# def distance(x1, y1, x2, y2):
#     return (((x2 - x1)**2 +(y2 - y1)**2))**0.5
#
# def triangle_perimetr(x1, y1, x2, y2, x3, y3):
#     a = distance(x1, y1, x2, y2)
#     b = distance(x2, y2, x3, y3)
#     c = distance(x3, y3 ,x1, y1)
#     return a + b + c
# print(triangle_perimetr(1, 2, 4, 5,6 ,7))

# # задача 8 найдите простое трехзначтное число
# def is_prime(n):
#     if n < 2: return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# primes = []
# for i in range(100, 1000):
#     if is_prime(i):
#         primes.append(i)
# print(primes)

# # Задача 9
# def sum_digits(n):
#     summa = 0
#     for d in str(n):
#         summa += int(d)
#     return summa
#
#
# def is_lucky(n):
#     s = str(n)
#     if sum_digits(s[:3]) == sum_digits(s[3:]):
#         print("Число счасливое ")
#     else:
#         print("Число не частливое ")
# is_lucky(112323)

# # 10 задача даны 6 различных чисел
# def max6(a, b, c, d, e, f):
#     return max(a, b, c, d, e, f)
# print(max6(1,2,4,5,6,7))

# Задача 13
# Даны основания и высоты	двух равнобедренных	трапеций. Найти	сумму их
# периметров и сумму их площадей.
# (Определить процедуру для расчета  периметра и площади равнобедренной
# трапеции по ее основаниям и высоте.)

# def trapezoid_permiter_area(a, b, h):
#     side = (((a - b) / 2) ** 2 + h ** 2) ** 0.5
#     p = a + b + 2 * side
#     area = (a + b) / 2 * h
#     return p, area
#
# trapezoid1 = trapezoid_permiter_area(4, 10, 3)
# trapezoid2 = trapezoid_permiter_area(6, 15, 5)
# print(f"Сумма переметров трапецией: {trapezoid1[0] + trapezoid2[0]}")
# print(f"Сумма площадей трапецией: {trapezoid1[1] + trapezoid2[1]}")

# задача 14
# В зависимости от выбора пользователя вычислить площадь
# круга, прямоугольника или треугольника
# Для вычисления площади каждой фигуры должна быть написана отдельная функция.

# def circle_area(r):
#     return 3.14 * r ** 2
#
# def rect_area(a, b):
#     return a * b
#
# def triangle_area(a, h):
#     return  (a * h) / 2
#
# print("1 - Круг")
# print("2 - Прямоугольник")
# print("3 - Треугольник")
# figure = input("Выберете фигуру, площадь которой вы хотите найти: ")
# if figure == "1":
#     r = float(input("Введите радиус круга: "))
#     print("Площадь круга:", circle_area(r))
# elif figure == "2":
#     a = float(input("Введите сторону a у прямоугольника: "))
#     b = float(input("Введите сторону b у прямоугольника: "))
#     print("Площадь прямоугольника:",rect_area(a, b))
# elif figure == "3":
#     a = float(input("Введите сторону треугольника: "))
#     h = float(input("Введите высоту треугольника, проведённую к этой стороне: "))
#     print("Площадь треугольника:",triangle_area(a, h))
# else:
#     print("Введена ошибочная команда")

# задача 16
# Напишите процедуру с параметрами n и s, которая выводит квадрат размером  nxn из символа,
# который вводится с клавиатуры. Используя эту процедуру,
# напишите программу, которая запрашивает два значения – строну квадрата и  символ,
# и вызывает процедуру рисования требуемого квадрата

# def draw_square(n, s):
#     for _ in range(n):
#         print(n * s)
#
# side = int(input("Введите сторону квадрата: "))
# symbole = input("Введите символ: ")
# draw_square(side, symbole)

# задача 17
# Напишите процедуру, которая выводит на экран все делители числа N
# в одну  строку через пробел. Используя данную процедуру, составьте программу,
# которая  для всех введенных натуральных чисел (числа вводятся до 0, 0 - признак окончания  ввода)
# выводит делители текущего числа.

# def print_divisors(n):
#     for i in range(1, n + 1):
#         if n % i == 0:
#             print(i, end=" ")
#     print()
#
# while True:
#     x = int(input("Введите число (0 для выхода из программы): "))
#     if x == 0:
#         break
#     print_divisors(x)

# задача 19
# Напишите логическую функцию pointInRect, которая возвращает значение True,
# если точка с заданными координатами находится внутри прямоугольника, для  которого заданы
# координаты верхнего левого и правого нижнего углов. Стороны  прямоугольника параллельны осям координат.

# def pointInRect(x, y, x1, y1, x2, y2):
#     return x1 <= x <= x2 and y2 <= y <= y1
#
# x = int(input("Введите координату x исходной точки: "))
# y = int(input("Введите координату y исходной точки: "))
#
# x1 = int(input("Введите координату x левого верхнего угла прямоугольника: "))
# y1 = int(input("Введите координату y левого верхнего угла прямоугольника: "))
# x2 = int(input("Введите координату x правого нижнего угла прямоугольника: "))
# y2 = int(input("Введите координату y правого нижнего угла прямоугольника: "))
#
# print(pointInRect(x, y, x1, y1, x2, y2))


# задача 20
# Напишите логическую функцию pointInTriangle, которая возвращает значение
# True,	если	точка	с	заданными	координатами	находится	внутри	треугольника,
# заданного координатами трёх своих вершин.

# def side_length(x1, y1, x2, y2):
#     return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#
# def heron_triangle_area(a, b, c):
#     p = (a + b + c) / 2
#     return (p * (p - a) * (p - b) * (p - c))**0.5
#
# def pointinTriangle(px, py, x1, y1, x2, y2, x3, y3):
#     # Стороны и площадь исходного треугольника ABC
#     a = side_length(x1, y1, x2, y2)
#     b = side_length(x2, y2, x3, y3)
#     c = side_length(x3, y3, x1, y1)
#     area_abc = heron_triangle_area(a, b, c)
#
#     # Стороны и площадь треугольника PAB
#     a1 = side_length(px, py, x1, y1)
#     b1 = side_length(px, py, x2, y2)
#     c1 = side_length(x1, y1, x2, y2)
#     area_pab = heron_triangle_area(a1, b1, c1)
#
#     # Стороны и площадь треугольника PBC
#     a2 = side_length(px, py, x2, y2)
#     b2 = side_length(px, py, x3, y3)
#     c2 = side_length(x2, y2, x3, y3)
#     area_pbc = heron_triangle_area(a2, b2, c2)
#
#     # Стороны и площадь треугольника PCA
#     a3 = side_length(px, py, x3, y3)
#     b3 = side_length(px, py, x1, y1)
#     c3 = side_length(x3, y3, x1, y1)
#     area_pca = heron_triangle_area(a3, b3, c3)
#
#     total_area = area_pab + area_pbc + area_pca
#
#     return round(total_area, 5) == round(area_abc, 5)
#
# print(pointinTriangle(1, 1, 0, 0, 4, 0, 0,3))


# пример рекурсии 1
# def F(n):
#     print(n)
#     if n < 5:
#         F(n + 1)
#         F(n + 3)
#
# F(1)

# пример рекурсии 2
# def F(n):
#     print(n)
#     if n > 1:
#         F(n - 1)
#         F(n - 3)
#
# F(6)

# пример проверки (get) и установки (set) глубины рекурсии
# import sys
#
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())

















