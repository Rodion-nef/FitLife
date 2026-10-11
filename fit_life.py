def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 1)
def calculate_water(weight):
    ml = weight * 30
    return round(ml / 1000, 1)
if __name__ == "__main__":
    print(f'Здравствуйте, я бот от FitLife.Я буду давать вам советы по правильному питанию.Давайте знакомиться ')
    user_name= input("Как вас зовут?")
    user_age=int(input("Сколько вам лет?"))
    print(f'Приятно познакомиться , {user_name}')
    user_weight=float(input('Укажите пожалуйста свой вес в кг,используя точку '))
    user_height=float(input('Укажите пожалуйста свой рост в метрах, используя точку '))
    bmi_result = calculate_bmi(user_weight, user_height)
    water_result = calculate_water(user_weight)
    water_ml = user_weight * 30 
    water_l = round (water_ml / 1000,1)                                
    print(f'Отчет для пользователя: ,{user_name}, {user_age},г.')
    print(f'Твой Индекс Массы Тела: ,{bmi_result}')
    print(f'Рекомендуемая норма воды: , {water_result}, л. в день')
    print(f'Расчет окончен. Будьте здоровы!')
