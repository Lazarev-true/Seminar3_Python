# Задайте список из нескольких чисел. Напишите 
# программу, которая найдёт сумму элементов 
# списка, стоящих на нечётной позиции.

from random import randint

N = 7

listOld = []
listNew = []

listOld = [(lambda i: randint(1, 20)) (i) for i in range(N)]
listNew = [j for j in listOld if (listOld.index(j) + 1) % 2 == 0]

print(f'{listOld} -> на нечётных позициях элементы {" и " .join(map(str, listNew))}, их сумма: {sum(listNew)}')