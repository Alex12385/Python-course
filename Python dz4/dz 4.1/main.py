# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]

a = [int(x) for x in input().split()]
k = set(a)

b = [int(x) for x in input().split()]
k1 = set(b)

lok = k & k1
kool = list(lok)
spisok = []
for el in k:
    if el in k1:
        spisok.append(el)
print(spisok)
kool.sort()
print(*kool)
