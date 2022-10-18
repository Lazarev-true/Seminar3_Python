# Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное

number = int(input('Введите число: '))
n = number
d = ''

if n == 0:
    print(f'{n} -> 0')

else:
    while number >= 1:
        d = str(number % 2) + d
        number = number // 2
 
    print(f'{n} -> {d}')
