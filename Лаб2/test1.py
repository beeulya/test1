money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month=0
live=True
while(live):
    money_capital+=salary
    if spend<money_capital:
        money_capital-=spend
        spend+=spend*increase
        month+=1
    else:
        live=False
print("Количество месяцев, которое можно протянуть без долгов:", int(month))
