# Входные данные
# Пользователь вводит строку. Выловите исключения, если введённая строка слишком
# короткая.
# Выходные данные
# Воспользуйтесь одним print(), но при этом выводите с новой строки:
#  Сначала выведите третий символ этой строки.
#  Во второй строке выведите предпоследний символ этой строки.
#  В третьей строке выведите первые пять символов этой строки.
#  В четвертой строке выведите всю строку, кроме последних двух символов.
#  В пятой строке выведите все символы с четными индексами (считая, что
# индексация начинается с 0, поэтому символы выводятся, начиная с первого).
#  В шестой строке выведите все символы с нечетными индексами, то есть начиная
# со второго символа строки.
#  В седьмой строке выведите все символы в обратном порядке.
#  В восьмой строке выведите все символы строки через один в обратном порядке,
# начиная с последнего.
#  В девятой строке выведите все символы в обратном порядке без первого и
# последнего элемента.
#  В десятой строке выведите длину данной строки.
str = input("Enter a string:")
i = 0
temp = ""
length=len(str)
try:
 while i<10:
    if i == 0:
        temp = str[2]
    elif i == 1:
         temp = str[length-2]
    elif i == 2:
        temp = str[0:6]
    elif i == 3:
        temp = str[0:-2]
    elif i == 4:
        temp = str[1:-1:2]
    elif i == 5:
        temp = str[2:-1:2]
    elif i == 6:
        temp = str[::-1]
    elif i == 7:
        temp = str[::-2]
    elif i == 8:
        temp = str[length-2:0:-1]
    else:
        temp = length
    i=i+1
    print(temp)
except:
    print("string has incorrect format")






