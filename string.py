## a = [1,2,3,11,12,32,11,-5]
# print(min(a))
# print(max(a))
# print(len(a))
# print(a[len(a)-1])
# print(a.index(12))
# print(a[3])
# print(a.count(11))

# string = "Привет мир!"
# print(string.count("!"))

# string = "привет мир, Как у Тебя дела? ещё одна фраза. а затем вторая"
# print(string.capitalize())
# print(string.title())
# print(string.upper())
# print(string.lower())
# print(string.swapcase())
#
# low = string.lower()
# print(low.isupper())
# print(low.islower())
# print(low.istitle())
#
# print(" - ".join(["Яблоко", "Груша"]))
#
# words = ["Привет", "мир"]
# result = " ".join(words)
# print(result)
#
# nums = [1, 2, 3]
# # print("".join(nums)) будет ошибка по типу данных
# print("-".join(map(str, nums)))
# print([str(x) for x in nums])
#
# print(string.split(" "))
#
# print(string.partition(" "))
#
# print(string.startswith("привет мир"))
# print(string.endswith("Вторая"))
#
# print(string.find("привет")) # начинается с 0 индекса
# print(string.find("мир")) # начинается с 7 индекса
# print(string.find("и")) # индекс первого вхождения (первой буквы "и") (индекс 2)
# print(string.find("абвгдеж")) # значение не найдено (фиксированный ответ -1)
# print(string.find("Привет")) # поиск регистрозависимый (первая буква в оригнале маленькая)
# # т.е. ничего не найдено (-1)
#
# print(string.find("и", 5)) # поиск начиная с 5-го индекса для буквы и (8 индекс)
# print(string.find("и", 3, 5)) # поиск начиная с 3-го по 5-й индекс
# # для буквы и (ничего не найдено в этом диапазоне, вернули -1)
#
# print(string.replace("мир", "Россия")) # замена старого на новое
# print("привет мир, пока мир".replace("мир", "Россия")) # заменяет все вхождения
# print("привет Мир, пока мир".replace("мир", "Россия")) # чувствителен к регистру


# 1. Напишите программу, которая принимает строку от пользователя и выводит ее в обратном порядке.
# s = input("Введите строку: ")
# print(s[::-1])

# 2. Напишите программу, которая принимает две строки и проверяет,
# являются ли они анаграммами (то есть состоят из одних и тех же символов в любом порядке).
# s1 = input("Введите первую строку: ").lower()
# s2 = input("Введите вторую строку: ").lower()
# print(sorted(s1) == sorted(s2))

# 3. Напишите программу, которая принимает строку и подсчитывает
# количество гласных и согласных букв в ней.
# s = input("Введите строку: ").upper()
# vowels = "АОУЭЫИЯЕЁЮ"
# consonants = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
# v = c = 0
# for char in s:
#     if char in vowels:
#         v += 1
#     elif char in consonants:
#         c += 1
# print("Гласных:", v)
# print("Согласных:", c)

# 4. Напишите программу, которая принимает строку и проверяет,
# является ли она палиндромом (то есть одинаково читается в обоих направлениях).
# s = input("Введите строку: ").lower().replace(" ", "")
# if s == s[::-1]:
#     print("Палиндром")
# else:
#     print("Строка не является палиндромом")
