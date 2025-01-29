# Модуль 4. Пространство имен и область видимости. Лекция 8.
# Ввод пользователем чисел через пробел
'''data = list(map(int, input('Введите числа через пробел: ').split()))'''

# module_4.alg:
'''def bubble_sort(ls):
    swap = True
    while swap:
        swap = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swap = True

def selection_sort(ls):
    for i in range(len(ls) - 1):
        low = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[low]:
                low = j
                ls[i], ls[low] = ls[low], ls[i]

# from module_4.alg import *
print(data)
bubble_sort(data)
print(data)
nums = [5,6,7,8,20,1,3]
selection_sort(nums)
print(nums)'''


# ==========================================================================
# Модуль 5. Классы и объекты

# объект — это переменная, созданная на основе класса,
# а класс представляет собой инструкцию или план, в котором описаны характеристики и способности объектов.
'''
class Human:
    pass
den = Human()
max = Human()
print(type(den))   # <class '__main__.Human'>
print(den == max)   # False  значения
print(den is max)   # False  объекты
print(id(den), id(max)) # 137387595842000 137387595842256 разные
'''


# Чтобы добавить уникальные характеристики при создании класса, в отношении объектов den и max необходимо
# использовать конструкцию 'def __init__' — инициализатор
# Этот метод вызывается один раз при создании объекта класса, что позволяет объекту получать уникальные
# характеристики. Все эти уникальные характеристики определяются внутри метода '__init__'.
'''
class Human:
    def __init__(self):     # self, является указателем на сам объект. 
        self.name = 'Den'
den = Human()       # self = den
max = Human()       # self = max
print(den.name, max.name)   # Den Den
'''
'''# возможность задавать имя вручную
class Human:
    def __init__(self, name, age, isStudent):
        self.name = name
        self.age = age
         
den = Human('Den', 15)
max = Human('Max', 25)
print(den.name, max.name)   # Den Max'''


# ----------------------------------------------------
# Атрибуты и методы объекта. Указатель на свой объект в методах

# Атрибуты представляют собой переменные внутри класса, а методы — функции, определенные внутри него.
# den.surname = 'Popov'

# Атрибуты можно как создавать, так и изменять уже существующие.
# den.age = 26

# Методы также можно использовать для добавления функциональности.
# Можно сделать вызов метода 'say_info' внутри метода '__init__' (например, 'self.say_info')
# метод '__init__' срабатывает один раз при создании объекта класса.
'''class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age} лет.')

den = Human('Den', 15)
max = Human('Max', 25)

den.say_info()
max.say_info()'''

