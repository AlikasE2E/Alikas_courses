#Пользователь вводит строку. Разрежьте её на две равные части (если длина строки —
# чётная, а если длина строки нечётная, то длина первой части должна быть на один
# символ больше). Переставьте эти две части местами, результат запишите в новую
# строку и выведите на экран.

first = input('Введи строку:')
second = len(first)
l1 = second - second // 2
print(first[l1:] + first[:l1])

