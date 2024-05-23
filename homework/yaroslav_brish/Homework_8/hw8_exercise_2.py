# Задание 2

# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел Фибоначчи.
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число.


import sys

# Увеличиваем ограничение на количество цифр в строковом представлении целого числа,
# т.к. дефолтное значение == 4300 digits.

sys.set_int_max_str_digits(1000000)  # Устанавливаем значение, достаточное для 100000-го числа Фибоначчи


def fibonacci():
    """ Генератор, который бесконечно генерирует числа Фибоначчи """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci_number(n: int):
    """ Функция получает n-ое число Фибоначчи """
    fib_generator = fibonacci()
    for _ in range(n):
        next(fib_generator)
    return next(fib_generator)


# print("5-е число Фибоначчи:", get_fibonacci_number(5))
# print("200-е число Фибоначчи:", get_fibonacci_number(200))
# print("1000-е число Фибоначчи:", get_fibonacci_number(1000))
# print("100000-е число Фибоначчи:", get_fibonacci_number(1000000))


def print_fibonacci_numbers(values: list):
    """
    Решил, что функцией на вывод значений будет красивее, чем повторять print в каждой строке.
    Да и в результате вывод получается быстрее. Правда, не знаю, почему... xD
    """
    for number in values:
        fib_number = get_fibonacci_number(number)
        print(f"{number}-е число Фибоначчи: {fib_number}")


fib_numbers_to_print = [5, 200, 1000, 100000]
print_fibonacci_numbers(fib_numbers_to_print)
