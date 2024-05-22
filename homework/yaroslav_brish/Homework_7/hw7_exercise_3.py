# Задание №3

def find_number(value: list):
    for item in value:
        number = int(item.split()[-1])
        print(number + 10)


operations = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

find_number(operations)
