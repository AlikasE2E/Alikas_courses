
#Определите является ли строка записью числа.
myString = "123456";  # True
print (myString.isdigit());

myStringTwo = "12.5"; # False
print(myStringTwo.isdigit());

myStringThree = "I am Alika";
print (myStringThree.isdigit()); # False

myStringFour = "12.5"; # False
print((myStringFour*10).isdigit());

myStringFive = "We look forward to 2019 year"; #False
print (myStringFive.isdigit());

myStringSix = "²3455";
print(myStringSix.isdigit());

#Посчитайте сколько у вас пробелов в строке.
countingSpaces = "Life is a damn short"
print(countingSpaces.isspace());

countingSpacesAgain = "     ";
print (countingSpacesAgain.isspace());

#Посчитайте сколько у вас символов точки . в строке.
lookingForDots = "Fire. Fall. Random. Words";
print(lookingForDots.count('.')); # 3

# Создайте строку &quot;Homework&quot;. Преобразуйте ее в строку длиной 100 символов,
# посередине которой исходное слово, а с обоих сторон строка заполнена
# пробелами. Выведите ее на экран.
stringWithSpaces = "Homework";
print(stringWithSpaces.center(100,' '));

#Сделайте первые буквы слов строки большими (upper case).
capital = "why do you cry, Willie? why do you cry? why, Willie, why, Willie why,Willie, why!?"
print(capital.title());

