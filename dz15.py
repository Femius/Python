# Задание 1:
# Создайте класс Rectangle, который будет содержать
# атрибуты width и height и методы area() и perimeter().
# Создайте класс Square, который будет наследовать
# класс Rectangle и содержать только атрибут side (а не
# width и height).
class Rectangle:
        width = ''
        height = ''
        def area(self):
            def perimeter(self):
                pass
class Square(Rectangle):
    side =""
    pass

# Задание 2:
# Создайте класс Person, который будет содержать
# атрибуты name, age, gender и метод introduce(), который
# будет выводить на экран информацию о человеке.
# Создайте класс Employee, который будет наследовать
# класс Person и содержать атрибуты salary и position, а
# также метод work(), который будет выводить на экран
# информацию о работе сотрудника.

class Person:
    def __init__(self,name, age, gender):
        self.name = name
        self.age =age
        self.gender = gender
    def __str__(self):
        return f"{self.name} | Возраст: {self.age} | Пол: {self.gender}"
class Employee(Person):
    def __init__(self,salary, position):
        self.salary = salary
        self.pisition = position
    def __str__(self,work):
        return f"{self.salary} |  {self.pisition}"








