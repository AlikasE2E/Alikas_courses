# Функция принимает три числа a, b, c. Функция должна определить, существует
# ли треугольник с такими сторонами и если существует, то возвращает тип
# треугольника Equilateral triangle (равносторонний), Isosceles triangle
# (равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not
# a triangle).
def triangle(a, b, c):
     if a == b == c:
         return("Equilateral triangle")
     elif a == b != c:
            return("Isosceles triangle")
     elif a!= b != c:
            return("Versatile triangle")
     elif (a < b+c) and (b < a+c) and (c < a+b):
         return("Triangle Exists")
result = triangle (6, 6, 5)
print(result)
