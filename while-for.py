# n = 5
# while n < 10:
#     n += 1
#     if n == 7:
#         continue
#     print(n)
# print("Цикл завершен")

# # Задание 8
# # Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000
# # — 5%, свыше 1000 — 8%. Пользователь вводит с клавиатуры уровень продаж для трех
# # менеджеров. Определить их зарплату, определить лучшего менеджера, начислить ему премию
# # 200$, вывести итоги на экран.
#
# sales1 = float(input("Введите уровень продаж первого менеджера"))
# sales2 = float(input("Введите уровень продаж второго менеджера"))
# sales3 = float(input("Введите уровень продаж третьего менеджера"))
# salaries = []
# for sales in [sales1, sales2, sales3]:
#     if sales <= 500:
#         percent = 0.03
#     elif sales1 <= 1000:
#         percent = 0.05
#     else:
#         percent = 0.08
#     salary = 200 + sales + percent
#     salaries.append(salary)
#
#
# # Определяем лучшего менеджера
# best_salary = max(salaries)
# best_index = salaries.index(best_salary)
# salaries[best_index] += 200
#
# print(f"Зарплата 1 менеджера: {salaries[0]}")
# print(f"Зарплата 2 менеджера: {salaries[1]}")
# print(f"Зарплата 3 менеджера: {salaries[2]}")
# print(f"Лучший менеджер: {best_index + 1}-ый")


# for x in range(5, 50, 5):
#     print(x)

# for x in range(50, 5, -5):
#     print(x)

# for x in enumerate(["Первы", "Второй", "Третий"]):
#     print(x)

# # 1. Задача о четных числах:
# Напишите программу, которая выводит все четные числа от 1 до 50.
# # 1 способ
# for i in range(2, 51, 2):
#     print(i)
# # 2 способ
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

# # 2. Задача о сумме чисел:
# Напишите программу, которая считает сумму всех чисел от 1 до 100.
# # 1 способ
# total = 0
# for i in range(1,101):
#     total += i
# print(total)
# # 2 способ
# print(sum(range(1, 101)))

# # 3. Задача о проверке простого числа:
# # Напишите программу, которая проверяет, является ли заданное число простым.
#
# number = int(input("Введите число: "))
# is_prime = True
# if number < 2:
#     is_prime = False
# else:
#     for i in range(2,number):
#         if number % i == 0:
#             is_prime = False
#             break
# if is_prime:
#     print("Число просто")
# else:
#     print("Число не являеться простым ")

# # 4. Задача о факториале числа:
# # Напишите программу, которая вычисляет факториал заданного числа.
#
# n = int(input("Введите число: "))
# result = 1
# for i in range(1, n +1):
#     result *= i
# print(result)

# 5. Задача о числах Фибоначчи:
# Напишите программу, которая выводит первые 10 чисел Фибоначчи.












