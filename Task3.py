# Задайте список из вещественных чисел. Напишите 
# программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

from random import uniform

list1 = []
list2 = []

N = 7

for i in range(N):
    list1.append(round(uniform(1, 10), 2))

    list2.append(list1[i] - (int(list1[i])))

min = min(list2)
max = max(list2)
dif = round((max - min), 2)

print(f'{list1} => {dif}')