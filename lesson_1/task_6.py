profit = int(input("Введите выручку фирмы "))
costs = int(input("Введите издержки фирмы "))
n = profit // costs
if profit > costs:
     print("Фирма работает с прибылью. Рентабельность выручки составила ", n)
     workers = int(input("Введите колличество сотрудников "))
     print("Выручка на каждого сотрудника составляет ", n // workers)
elif profit == costs:
     print("Фирма работает в ноль")
else:
     print("Фирма работает в убыток")