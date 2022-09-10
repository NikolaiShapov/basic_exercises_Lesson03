# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
print('Дан список учеников, нужно посчитать количество повторений каждого имени ученика:')
list_names =[]
for names in students:
    list_names.append(names['first_name'])
for name in set(list_names):
    count_name = list_names.count(name)
    print(f'{name}: {count_name}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
    {'first_name': 'Вася'},
]
print('\nДан список учеников, нужно вывести самое часто повторящееся имя:')
list_names =[]
for names in students:
    for key,items in names.items():
        list_names.append(items)

from collections import Counter

dict_count = Counter(list_names)
max_count_name = max(dict_count.values())
print('Самое частое имя среди учеников: ', end = '')
for item in dict_count:
    if dict_count[item] == max_count_name:
        print(item, end = ' ')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
        {'first_name': 'Петя'},
    ],
]
print('\nЕсть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе:')
from collections import Counter

for number_class, students in enumerate(school_students, start =1):
    list_names =[]
    name_count = []
    for names in students:
        list_names.append(names['first_name'])
    dict_count = Counter(list_names)
    max_count_name = max(dict_count.values())
    if list(dict_count.values()).count(max_count_name) > 1:
        for item in dict_count:
            if dict_count[item] == max_count_name:
                name_count.append(item)
    else:
        name_count = max(dict_count, key = dict_count.get)
    print(f' Самое частое имя в классе {number_class}: {name_count}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
print(f'\nДля каждого класса нужно вывести количество девочек и мальчиков в нём:')
for school_class in school:
    number_class = school_class['class']
    male = 0
    women = 0
    for stud in school_class['students']:
        name = stud['first_name']
        if is_male.get(name):
            male += 1
        else:
            women += 1
    print(f'Класс {number_class}: девочки {women}, мальчики {male}')

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
print('\nПо информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков:')
list_male_school = []
list_women_school = []
for school_class in school:
    number_class = school_class.get('class')
    male = 0
    women = 0
    for stud in school_class.get('students'):
        name = stud.get('first_name')
        if is_male.get(name):
            male += 1
        else:
            women += 1
    list_male_school.append((number_class, male))
    list_women_school.append((number_class, women))

dict_male_school = dict(list_male_school)
dict_women_school = dict(list_women_school)
max_class_male = max(dict_male_school, key = dict_male_school.get) # корректоно работает если только одно значение в словаре > других, если два имени встречаются одиноковое количество раз => логику надо переписать/дописать!
max_class_women = max(dict_women_school, key = dict_women_school.get) # корректоно работает если только одно значение в словаре > других, если два имени встречаются одиноковое количество раз => логику надо переписать/дописать!

print(f'Больше всего мальчиков в классе {max_class_male}')
print(f'Больше всего девочек в классе {max_class_women}')
