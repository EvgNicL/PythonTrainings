first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second and first == third:
    print(0)
elif first == second or first == third or third == second:
    print(2)
else:
    print(3)