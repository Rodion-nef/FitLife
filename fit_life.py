print(f'Здравствуйте, я бот от FitLife.Я буду давать вам советы по правильному питанию.Давайте знакомиться ')
user_name= input("Как вас зовут?")
user_age=int(input("Сколько вам лет?"))
print(f'Приятно познакомиться , {user_name}')
user_weight=float(input('Укажите пожалуйста свой вес в кг,используя точку '))
user_height=float(input('Укажите пожалуйста свой рост в метрах, используя точку '))
#bmi = round (user_weight / (user_height ** 2),1)                    #расчёт индекса массы тела
def bmi(user_weight,user_height):
    return round(user_weight / (user_height ** 2),1)
water_ml = user_weight * 30 
water_l = round (water_ml / 1000,1)                                 #расчет нормы воды
print(f'Отчет для пользователя: ,{user_name}, {user_age},г.')
print(f'Твой Индекс Массы Тела: ,{bmi(user_weight, user_height)}')
print(f'Рекомендуемая норма воды: , {water_l}, л. в день')
print(f'Расчет окончен. Будьте здоровы!')
