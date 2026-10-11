def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 1)
def calculate_water(weight):
    ml = weight * 30
    return round(ml / 1000, 1)
if __name__ == "__main__":
    print('Здравствуйте, я бот от FitLife.')
    user_name = input("Как вас зовут?")
    user_age = int(input("Сколько вам лет?"))
   # print(f'Приятно познакомиться {user_name}')
    user_weight = float(input('Укажите пожалуйста ' \
    'свой вес в кг,используя точку '))
    user_height = float(input('Укажите пожалуйста' \
    ' свой рост в метрах, используя точку '))
    bmi_result = calculate_bmi(user_weight, user_height)
    water_result = calculate_water(user_weight)                               
    print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
    print(f'Твой Индекс Массы Тела: {bmi_result}')
    print(f'Рекомендуемая норма воды: {water_result} л. в день')
    print('')
    print('Расчет окончен. Будьте здоровы!')
