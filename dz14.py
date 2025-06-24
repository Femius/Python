# Задача 1
# Что вернется при вызове F4
def F(n):
    if n >2:
     return F(n-1) + G(n - 2)
    else:return n
def G(n):
    if n >2:
     return G(n-1) + F(n-2)
    else:return n + 1
print(F(4))
# Ответ 7

# Напишите рекурсивную функцию fibonacci(n),
# которая принимает на вход целое неотрицательное
# число n и возвращает n-е число Фибоначчи.

def fibonacci(n):
    if n in (1,2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))









