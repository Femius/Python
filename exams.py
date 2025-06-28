# # Задача 1: Простой калькулятор
# # Напишите программу, которая запрашивает у пользователя два числа и оператор (+, -, *, /),
# # а затем выполняет соответствующую операцию и выводит результат.
# number1 = float(input("Введите первое число: "))
# number2 = float(input("Введите второе число: "))
# operator =input("Введите оператор (+, -, *, /): ")
# def calculator():
#     if operator == '+':
#         result = number1 + number2
#     elif operator == '-':
#         result = number1 - number2
#     elif operator == '*':
#         result = number1 * number2
#     elif operator == '/':
#         result = number1 / number2
#     print("Ответ:", result)
# calculator()


# Поиск наибольшего общего делителя (НОД)
# Напишите программу, которая запрашивает у пользователя два числа и выводит их наибольший общий делитель (НОД).

def nod(a,b):
    while b:
     a,b = b, a%b
    return a
a = int(input("Введите первое число:"))
b = int(input("Введите второе число: "))
print(nod(a,b))

