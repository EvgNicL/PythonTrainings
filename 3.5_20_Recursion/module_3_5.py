def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    return first * get_multiplied_digits(int(str_number[1:]))

n = get_multiplied_digits(40203)
print(n)

# При преобразовании строки(str) в число(int) первые нули убираются.
# int('00123') -> 123.
