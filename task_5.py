profit = int(input("Введите выручку фирмы "))
costs = int(input("Введите издержки фирмы "))
n = profit - costs
if profit > costs:
     print("Фирма работает с прибылью. Рентабельность выручки составила ", n)
elif profit == costs:
     print("Фирма работает в ноль")
else:
     print("Фирма работает в убыток")