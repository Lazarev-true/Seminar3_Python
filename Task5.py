# # Задайте число. Составьте список чисел Фибоначчи, 
# # в том числе для отрицательных индексов.

k = int(input('Задайте число: '))

list1 = [0] * (k + 1)
list2 = [1] * k

list1[1] = 1
list2[-2] = -1

for i in range(2, k + 1):
    list1[i] = list1[i - 1] + list1[i - 2]

for i in  reversed(range(-k, -2, 1)):
    list2[i] = list2[i + 2] - list2[i + 1]

print(f'Для k = {k} список Фибоначчи будет выглядеть так: {list2 + list1}')
#print(list1)
