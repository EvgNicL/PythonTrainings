grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

i = 0

while i < len(grades):
    grades[i] = sum(grades[i]) / len(grades[i])
    i = i + 1

students = sorted(list(students))
dict_ = dict(zip(students, grades))

print(dict_)