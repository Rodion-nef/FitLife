def calculate_bmi(weight, height):
    """Вычисляет индекс массы тела."""
    return round(weight / (height ** 2), 1)


def calculate_water(weight):
    """Вычисляет рекомендуемую норму воды в литрах."""
    ml = weight * 30
    return round(ml / 1000, 1)


if __name__  ==  "__main__":
    user_name = input()
    user_age = int(input())
    user_weight = float(input())
    user_height = float(input())
    bmi_result = calculate_bmi(user_weight, user_height)
    water_result = calculate_water(user_weight)
    print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
    print(f'Твой Индекс Массы Тела: {bmi_result}')
    print(f'Рекомендуемая норма воды: {water_result} л. в день')
    print()
    print('Расчет окончен. Будьте здоровы!')
