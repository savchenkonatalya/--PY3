salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(0, months):
    need_money +=spend
    spend*= (1+increase)


# TODO Оформить решение
need_money-=salary*months


print(round(need_money))
