#Присвоение переменной input_text введённой пользователем строки
input_text = input('Укажите год, на который необходимо составить календарь: ')
print()

#Приведение строки введённой пользователем посредством функции int() к числу и присвоение этого значения переменной year
year = int(input_text)

#Создание списка месяцев
months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

#Функция вычисления високосного года
def is_leap_year(year):
    if year % 4 != 0:
        is_leap = False  #Если остаток от деления года на 4 не равен 0, то год не високосный
    else:
        is_leap = True   #Если остаток от деления года на 4 равен 0, то год високосный
    if year % 100 == 0:
        is_leap = False  #Если остаток от деления года на 100 равен 0, то год не високосный
    if year % 400 == 0:
        is_leap = True   #Если остаток от деления года на 400 равен 0, то год високосный
    return is_leap       #returnn возвращает значение функции is_leap_year

#Функция вычисления количества дней в месяце
def get_duration(year_value, month_index):
    if month_index in [3, 5, 8, 10]:                        #Индексы месяцев в которых 30 дней
        duration = 30
    elif month_index == 1:                                  #Индекс месяца Февраль
        duration = 29 if is_leap_year (year_value) else 28  #Тернарный оператор и функция is_leap_year определяют
    else:                                                   #количество дней в Феврале введённого года
        duration = 31                                       #В противном случае 31 день
    return duration

#Функция печати дат месяца
def print_days(days_in_month, start_day):
    print('    ' * start_day, end='')         #Отступ до 1го числа недели
    for day in range(1, days_in_month + 1):   #Диапазон от первого до последнего дня месяца
        if day < 10:
            print('', day, end='  ')          #Дополнительные отступы для чисел из одной цифры
        else:
            print(day, end='  ')              #Отступ между числами
        if (day + start_day) % 7 == 0:
            print()                           #Перенос на новую неделю
    if (days_in_month + start_day) % 7 != 0:
        print()                               #Перенос, если месяц закончился не в воскресенье

#Функция печати шапки месяца
def print_header(year_value, month_index):
    print(months[month_index], year_value)
    print('ПН, Вт, Ср, Чт, Пт, Сб, Вс')

#Функция Кристиана Целлера вычисления дня недели, который приходится на 1 января
def get_starting_day(year):
    d = 1
    m = 13
    y = year -1
    h = (d + (13 *(m + 1)) // 5 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return (h + 5) % 7

#Функция вычисления дня недели, на который выпадает первое число следующего месяца
def adjust_start_day(start_day, days_in_month):
    result = (start_day + days_in_month) % 7
    return result

#Функция запуска программы
def print_calendar(year):
    #Вычисление дня недели, на который приходится 1 января year
    start_day = get_starting_day(year)
    #Вызов необходимых функций в цикле
    for month_number in range(12):
        print_header(year, month_number)
        duration = get_duration (year, month_number)
        print_days(duration, start_day)
        start_day = adjust_start_day(start_day, duration)
        print()

#ПУСК
print_calendar(year)
