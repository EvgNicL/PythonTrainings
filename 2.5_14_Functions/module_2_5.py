def get_matrix(n, m, value):
    matrix = []
    for r in range(n):      # Вложенный список - это строка матрицы
        row = []
        for c in range(m):  # элементы вложенных списков(глубже) - это столбцы матрицы
            row.append(value)
        matrix.append(row)
    return  matrix

res = get_matrix(3, 5, '*')

print(res)