#Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести
#одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

a = input("a:")
b = input("b:")
c = input("c:")
if (a == b) and (a == c) and (b == c):
     print
elif(a == b) or (a == c) or (b == c):
     print(2)
else:
     print(0)
