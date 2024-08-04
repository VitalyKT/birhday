import datetime

def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.day, today.month) < (birth_date.day, birth_date.month))
    return age

day = int(input('Введите день рождения:\n'))
month = int(input('Введите месяц рождения: \n'))
year = int(input('Введите год рождения:\n'))



birth_date = datetime.date(year, month, day)
print(f"Возраст: {calculate_age(birth_date)} лет")

