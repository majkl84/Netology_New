#########################Задание - 1#########################################
print("Кредитный калькулятор ")
base_rate = 10
federal_district = input("Вы с Дальнего востока да/нет?\n ").lower()
if federal_district == "да":
    print("Ставка по кредиту 2% ")
else:
    children = int(input("Сколько у вас детей?\n"))
    salary_project = input("Есть у вас зарплатный проект да/нет?\n ").lower()
    insurance = input(
        "Будите ли вы оформлять страховку в этом банке да/нет?\n ").lower()
    if children >= 3:
        base_rate -= 2
    if salary_project == "да":
        base_rate -= 0.5
    if insurance == "да":
        base_rate -= 1.5
    print("Ставка по кредиту ", base_rate)

#########################Задание - 1#########################################
print("Какой у вас знак зодиака")
month = input("Введите месяц рождения:\n").capitalize()
data = int(input("Введите день рождения:\n"))
if (month == 'Март' and 21 <= data <= 31) or (month == 'Апрель'
                                              and 1 <= data <= 19):
    print("Ваш знак зодиака Овен")
elif (month == 'Апрель' and 20 <= data <= 30) or (month == 'Май'
                                                  and 1 <= data <= 20):
    print("Ваш знак зодиака Телец")
elif (month == 'Май' and 21 <= data <= 31) or (month == 'Июнь'
                                               and 1 <= data <= 20):
    print("Ваш знак зодиака Близнецы")
elif (month == 'Июнь' and 21 <= data <= 30) or (month == 'Июль'
                                                and 1 <= data <= 22):
    print("Ваш знак зодиака Рак")
elif (month == 'Июль' and 23 <= data <= 31) or (month == 'Август'
                                                and 1 <= data <= 22):
    print("Ваш знак зодиака Лев")
elif (month == 'Август' and 23 <= data <= 31) or (month == 'Сентябрь'
                                                  and 1 <= data <= 22):
    print("Ваш знак зодиака Дева")
elif (month == 'Сентябрь' and 23 <= data <= 30) or (month == 'Октябрь'
                                                    and 1 <= data <= 22):
    print("Ваш знак зодиака Весы")
elif (month == 'Октябрь' and 23 <= data <= 31) or (month == 'Ноябрь'
                                                   and 1 <= data <= 21):
    print("Ваш знак зодиака Скорпион")
elif (month == 'Ноябрь' and 22 <= data <= 30) or (month == 'Декабрь'
                                                  and 1 <= data <= 21):
    print("Ваш знак зодиака Стрелец")
elif (month == 'Декабрь' and 22 <= data <= 31) or (month == 'Январь'
                                                   and 1 <= data <= 19):
    print("Ваш знак зодиака Козерог")
elif (month == 'Январь' and 20 <= data <= 31) or (month == 'Февраль'
                                                  and 1 <= data <= 18):
    print("Ваш знак зодиака Водолей")
elif (month == 'Февраль' and 19 <= data <= 29) or (month == 'Март'
                                                   and 1 <= data <= 20):
    print("Ваш знак зодиака Рыба")
else:
    print('Возможно вы ввели не правильно месяц или дату!')
