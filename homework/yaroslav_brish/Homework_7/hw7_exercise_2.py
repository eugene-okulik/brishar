# Задание №2

# Выведите на экран каждый ключ столько раз сколько указано в значении.
# Сделайте так, чтобы каждый ключ печатался в одной строке

words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for key, value in words.items():
    print(key * int(value))
