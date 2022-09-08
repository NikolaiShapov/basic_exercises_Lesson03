# Вывести последнюю букву в слове
word = 'Архангельск'
symbol_end = word[-1]
print(f'Вывести последнюю букву в слове "Архангельск": {symbol_end}' )


# Вывести количество букв "а" в слове
word = 'Архангельск'
count_symbol = word.lower().count('а')
print(f'Вывести количество букв "а" в слове "Архангельск": {count_symbol}')


# Вывести количество гласных букв в слове
word = 'Архангельск'
number_symbol = 0
for symbol in ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']:
    if symbol in word.lower():
        number_symbol += word.lower().count(symbol)
print(f'Вывести количество гласных букв в слове: "Архангельск": {number_symbol}')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
count_word = len(sentence.split())
print(f'Вывести количество слов в предложении "Мы приехали в гости": {count_word}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print('Вывести первую букву каждого слова на отдельной строке:')
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
len_word = 0
count = 0
for word in sentence.split():
    len_word += len(word)
    count += 1
sred_len = len_word / count
print(f'Усреднённая длина слова в предложении: {sred_len}')
