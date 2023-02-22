# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

n = int(input('Введите шестизначный номер билета: '))

num1 = n // 100000
num2 = (n // 10000) % 10
num3 = (n // 1000) % 10
num4 = (n // 100) % 10
num5 = (n // 10) % 10
num6 = (n % 10)
if num1 + num2 + num3 == num4 + num5 + num6:
    print(f"{(n)} -> Вам выпал счастливый билет!")
else:
    print(f"{(n)} -> К сожалению ваш билет несчастен")
