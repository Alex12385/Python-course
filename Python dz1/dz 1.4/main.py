# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no


a = int(input())
b = int(input())
k = int(input())
if k <= b * a and (k%a == 0 or k%b == 0):
    print('yes')
else:
    print('no')