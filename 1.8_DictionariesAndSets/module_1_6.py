# Работа со словарями:
my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict["Vasya"]}')
print(f"Not existing value: {my_dict.get('Tonia')}")
my_dict.update({'Tonia': 1982, 'Vera': 2001})
print(f"Deleted value: {my_dict.pop('Egor')}")
print(f'Modified dictionary: {my_dict}')
print()

# Работа с множествами:
my_set = {1, 1, 1, 'Яблоко', 'Яблоко', 42.314}
print('Set:', my_set)
my_set.add(15)
my_set.update({13, (5, 6, 1.6)})
my_set.remove(15)
print('Modified set:', my_set)


