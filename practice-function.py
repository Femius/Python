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
def distance(x1, y1, x2, y2):
    return (((x2 - x1)**2 +(y2 - y1)**2))**0.5

def triangle_perimetr(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3 ,x1, y1)
    return a + b + c
print(triangle_perimetr(1, 2, 4, 5,6 ,7))
























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
























