# Задайте список из нескольких чисел. Напишите 
# программу, которая найдёт сумму элементов 
# списка, стоящих на нечётной позиции.

from random import randint

N = 5

listOld = []
listNew = []

for i in range(N):
    listOld.append(randint(1, 20))
    if i % 2 != 0:
        listNew.append(listOld[i])

print(f'{listOld} -> на нечётных позициях элементы {" и " .join(map(str, listNew))}, их сумма: {sum(listNew)}')