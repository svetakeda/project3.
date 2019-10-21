# Student wants to buy a new laptop. This program counts all his expenses and incomes
# and then counts how many months would it take to earn this money. Then it shows his monthly revenue.

first_sum = int(input("Введите первоначальную сумму накоплении: "))  # Program asks information about students' incomes.
cost = int(input("Введите стоимость нового ноутбука: "))
income = int(input("Заработная плата студента: "))
expenses = int(input("Ежемесячные расходы студента: "))
investments = income - expenses
print ("Тогда его накопления будут выглядеть так:")
for num in range(first_sum, cost, investments):                     # It counts amount of time.
    print(num)
    months = int(cost / (first_sum + investments))
if months <= 12:
    print("Он сможет купить ноутбук через", months, "месяцев")      # It shows how many months would it take to earn it.
elif months > 12 and months <= 24:
    months3 = int(months - 12)
    print("Он сможет купить ноутбук через 1 год и", months3, "месяцев")
elif months > 24 and months <= 36:
    months2 = int(months - 24)
    print("Он сможет купить ноутбук через 2 года и", months2, "месяцев")
else:
    print("Для покупки нового ноутбука ему надо будет копить больше 2 лет")

