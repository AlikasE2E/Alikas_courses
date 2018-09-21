import math
from decimal import Decimal

#1.Вычислите длину гипотенузы в прямоугольном треугольнике со сторонами 179 и 971
hypotenuse = math.pow(179,2) + math.pow(971,2);
hypotenuseSqrt = (math.sqrt(hypotenuse));
print(math.ceil(hypotenuseSqrt)); # округлила до целого

#2. Дано двузначное число. Найдите число десятков в нем.
twoDigitNumber = 29;
print(twoDigitNumber/10);

#3.Дано трёхзначное число. Найдите сумму его цифр.
threeDigitNumber = 297;
print(2+9+7);

#4.Дано целое число n. Выведите следующее за ним чётное число.
a= 5;
print(a+2-(a%2));

#5.Дано положительное действительное число X. Выведите его дробную часть.
x = Decimal('17.9')
print(x - int(x))

#6.Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.
x = float(input())
print(int(x * 10) % 10)


