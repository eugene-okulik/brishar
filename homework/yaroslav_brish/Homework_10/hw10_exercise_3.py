# Задание №3

# Напишите программу:
# Есть функция, которая делает одну из арифметических операций
# с переданными ей числами (числа и операция передаются в аргументы функции).

# Программа спрашивает у пользователя 2 числа (вне функции)
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
#   - если числа равны, то функция calc вызывается с операцией сложения этих чисел
#   - если первое больше второго, то происходит вычитание второго из первого
#   - если второе больше первого - деление первого на второе
#   - если одно из чисел отрицательное - умножение


def operation_decorator(func):
    def wrapper(first, second):
        # operation = None - я так и не понял, нужно ли объявлять переменную заранее, но работает и без объявления
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        else:  # Этот случай соответствует (second > first)
            operation = '/'

        return func(first, second, operation)

    return wrapper


@operation_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second

# print(calc(-10, 4))
# print(calc(10, 4))
# print(calc(1, 4))
# print(calc(4, 4))
