money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов


n = money_capital
e = spend
months = 0
while True:
    n += salary
    if n >= e:
        months += 1
        n -= e
        e *= (1 + increase)

    else:
        break
print("Количество месяцев, которое можно протянуть без долгов:", months)