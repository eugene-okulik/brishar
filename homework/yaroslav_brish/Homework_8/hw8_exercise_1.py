# Задание №1

import random

# Запрашиваем у пользователя значение зарплаты
salary = int(input("Введите вашу зарплату: "))

# Назначаем случайное значение переменной bonus
bonus = random.choice([True, False])

# Если bonus - True, добавляем к зарплате случайный бонус:
# я выбрал в пределах от 1$ до 1000$
if bonus:
    random_bonus = random.randint(1, 1000)
    total_salary = salary + random_bonus
else:
    total_salary = salary

print(f"{salary}, {bonus} - '${total_salary}'")
