# Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.

from random import randint
from numpy import multiply
from math import ceil

listOld = []
listNew = []
N = 5
n = ceil(N / 2)

for i in range(N):
    listOld.append(randint(1, 10))
listNew = multiply(listOld, list(reversed(listOld)))
print(f'{listOld} => {listNew[:n]}')