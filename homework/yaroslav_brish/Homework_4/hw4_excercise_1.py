# Создайте словарь (и сохраните его в переменную my_dict)
# с такими ключами: ‘tuple’, ‘list’, ‘dict’, ‘set’.

my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': ['one', 'two', 'three', 'four', 'five'],
    'dict': {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': 1964,
        'color': ('red', 'white'),
        'country': 'USA'
    },
    'set': {'apple', True, 'cherry', 'banana', 99}
}

# Для того, что хранится под ключом ‘tuple’:
#   - выведите на экран последний элемент

print(my_dict['tuple'][-1])

# Для того, что хранится под ключом ‘list’:
#   - добавьте в конец списка еще один элемент
#   - удалите второй элемент списка

my_dict['list'].append('six')
my_dict['list'].remove('two')

# Для того, что хранится под ключом ‘dict’:
#   - добавьте элемент с ключом ('i am a tuple') и любым значением
#   - удалите какой-нибудь элемент

my_dict['dict'].update({'i am a tuple': 'WTF'})
my_dict['dict'].pop('country')

# Для того, что хранится под ключом ‘set’:
#   - добавьте новый элемент в множество
#   - удалите элемент из множества

my_dict['set'].add(False)
my_dict['set'].discard('apple')

# В конце выведите на экран весь словарь

print(my_dict)
