
# Создайте строку, в которой написан, какой-то текст. Пример:
# We are not what we should be!d
# We are not what we need to be.
# But at least we are not what we used to be
# (Football Coach)
#  Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
spisok = input("ведите свой текст и мы посчитаем:")
a = (spisok.split())
print (len(spisok.split()))
#  Удалите знаки препинания (пройдитесь циклом все слова и удалите
# методом strip знаки препинания)
some_list = 'We are not what we should be!d We are not what we ' \
           'need to be. But at least we are not what we used to be '\
           '(Football Coach)'
splitted = some_list.split(" ")
for word in splitted:
    print(word.strip('!,?,.,,,:,;,-,"()'))
#  Выведите слова в алфавитном порядке (найдите метод списка, который
# сортирует)
some_list = 'We are not what we should be!d We are not what we ' \
           'need to be. But at least we are not what we used to be '\
           '(Football Coach)'
first_split = some_list.split()
sort_some_list = sorted(first_split)
print(sort_some_list)
# Усложнённое ** (можно сначала его не делать):
#  Посчитать, сколько раз встречается каждое слово.
# (Подсказка: создавать словарь, где ключи — это слова из текста, а в значениях
# подсчитываем количество «встречаний» этого слова)
