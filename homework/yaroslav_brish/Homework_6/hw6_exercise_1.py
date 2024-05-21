# Задание №1

# Необходимо к каждому слову в тексте добавить 'ing' и вывести результат на экран.
# Знаки препинания должны сохраниться и не должны оказаться внутри нового слова.

text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

# print(text.split())

new_text = []
for word in text.split():
    if word[-1] in ',.':
        new_text.append(word[:-1] + 'ing' + word[-1:])
    else:
        new_text.append(word + 'ing')
print(' '.join(new_text))
