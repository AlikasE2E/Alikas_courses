# Это уже было, но теперь оформите это функцией:
# 1) Написать функцию is_year_leap, принимающую 1 аргумент — год, и
# возвращающую True, если год високосный, и False иначе.

def check_if_leap(input):
    if (((input % 4 == 0) & (input % 100 > 0))|(input % 400 == 0)):
        return True
    else:
        return False

result = check_if_leap(int(input('Enter year:')))
print(result)

# 2) Функция принимает три числа a, b, c. Функция должна определить,
# существует ли треугольник с такими сторонами. Если треугольник
# существует, вернёт True, иначе False.

def check_if_exists(a, b, c):
    if (a < b+c) and (b < a+c) and (c < a+b):
        return ('Треугольник существует.')
    else:
        return ('Треугольник не существует.')

result = check_if_exists(3,4,5)
print(result)
