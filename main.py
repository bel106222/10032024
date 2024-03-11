# Задание 1
# Пользователь вводит с клавиатуры номер дня недели (1-7).
# Необходимо вывести на экран названия дня недели. 
# Например, если 1, то на экране надпись понедельник,
# 2 - вторник и т.д.
print('ЗАДАНИЕ 1')
day = int(input('Введите номер дня недели:\n>'))
if day == 1:
    print('Это понедельник')
elif day == 2:
    print('Это вторник')
elif day == 3:
    print('Это среда')
elif day == 4:
    print('Это четверг')
elif day == 5:
    print('Это пятница')
elif day == 6:
    print('Это суббота')
elif day == 7:
    print('Это воскресенье')
else:
    print('Неверный номер дня недели')
print('############################################')
# Задание 2
# Пользователь вводит с клавиатуры номер месяца (1-12).
# Необходимо вывести на экран название месяца. Например, 
# если 1, то на экране надпись январь, 2 — февраль и т.д. 
print('ЗАДАНИЕ 2')
month = int(input('Введите номер месяца:\n>'))
if month == 1:
    print('Это январь')
elif month == 2:
    print('Это февраль')
elif month == 3:
    print('Это март')
elif month == 4:
    print('Это апрель')
elif month == 5:
    print('Это май')
elif month == 6:
    print('Это июнь')
elif month == 7:
    print('Это июль')
elif month == 8:
    print('Это август')
elif month == 9:
    print('Это сентябрь')
elif month == 10:
    print('Это октябрь')
elif month == 11:
    print('Это ноябрь')
elif month == 12:
    print('Это декабрь')
else:
    print('Неверный номер месяца')
print('############################################')
# Задание 3
# Пользователь вводит с клавиатуры число. Если число
# больше нуля, нужно вывести надпись «Number is positive»,
# если меньше нуля, «Number is negative», если равно нулю -
# «Number is equal to zero».
print('ЗАДАНИЕ 3')
number = int(input('Введите число:\n>'))
if number > 0:
    print('Numberis positive')
elif number < 0:
    print('Number is negative')
else:
    print('Number is equal to zero')
print('############################################')
# Задание 4
# Пользователь вводит два числа. Определить, равны
# ли эти числа, и, если нет, вывести их на экран
# в порядке возрастания.
print('ЗАДАНИЕ 4')
number1 = int(input('Введите первое число:\n>'))
number2 = int(input('Введите второе число:\n>'))
if number1 != number2:
    if number1 > number2:
        print(number2, ',', number1)
    else:
        print(number1, ',', number2)
else:
    print('Числа равны')
print('############################################')
    