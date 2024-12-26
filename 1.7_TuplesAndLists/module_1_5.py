# 2. Задайте переменные разных типов данных:
immutable_var = (1, 2, 'a', 'b')
print('\nImmutable tuple: ', immutable_var)

# 3. Изменение значений переменных:
# immutable_var[3] = 'change'
print("'tuple' object does not support item assignment")

# 4. Создание изменяемых структур данных:
mutable_list = [1, 2, 'a', 'b', 'Modified']
mutable_list[2:4] = [True, False]
print(f'\n{mutable_list}')