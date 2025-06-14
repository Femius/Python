# # Напишите функцию, которая вычисляет среднее
# # арифметическое пяти целых чисел.
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# num4 = int(input("Введите четвертое число: "))
# num5 = int(input("Введите пятое число: "))
#
# def nums(num1, num2, num3, num4, num5):
#     return (num1 + num2 + num3 + num4 +num5) / 5
# i = nums(num1, num2, num3, num4, num5)
# print(f"Среднее арифметическое: {i}")

# # Напишите функцию, которая находит количество
# # цифр в десятичной записи числа.
#
# nums = int(input("Введите ваше число:"))
# def num():
#     return len(str(nums))
# num()
# print("Количество цифр", num())

# Найти периметр треугольника, заданного
# координатами своих вершин. (Определить функцию
# для расчета длины отрезка по координатам его
# вершин.)

def distance(x1, y1, x2, y2):
    return (((x2 - x1)**2 +(y2 - y1)**2))**0.5

def triangle_perimetr(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3 ,x1, y1)
    return a + b + c
print(triangle_perimetr(1, 2, 4, 5,6 ,7))





























