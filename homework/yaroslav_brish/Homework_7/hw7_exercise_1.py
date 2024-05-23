# Задание №1

number = 21
user_input = int(input("Угадайте цифру: "))

while user_input != number:
    user_input = int(input("Попробуйте снова: "))

print("Поздравляю! Вы угадали!")
