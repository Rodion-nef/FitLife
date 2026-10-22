MILLILITRS_KG = 30
print('Здравствуйте, я бот от FitLife')
user_name = input('Как зовут?')
user_age = int(input('Ваш возраст? Укажите в цифрах'))
user_weight = float(input('Вес'))
user_height = float(input('Рост'))
bmi = (user_weight / (user_height ** 2))
water_ml = user_weight * MILLILITRS_KG
water_l = water_ml / 1000
print(f'Отчет для пользователя {user_name}  {user_age} полных лет')
print(f'Твой Индекс Массы Тела: {round(bmi, 1)}')
print(f'Рекомендуемая норма воды: {water_l} л.')
