#Даны два неупорядоченных набора целых чисел (может быть, с 
#повторениями). Выдать без повторений в порядке возрастания 
#все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого 
#множества. m - кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.

from random import randint

print('введите длинну первого массива:')
n =int(input())
list_1 = list()
for i in range(n):
    list_1.append(randint(0, 10))
print(list_1)

print('введите длинну второго массива:')
m =int(input())
list_2 = list()
for i in range(m):
    list_2.append(randint(0, 10))
print(list_2)

k = set(list_1)
k1 = set(list_2)

lok = k & k1
kool = list(lok)

print(kool)