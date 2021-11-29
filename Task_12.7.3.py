per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму вклада: "))
deposit = [round(float(money * i / 100), 2) for i in list(per_cent.values())]
print(deposit)
print(max(deposit))
# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# money = float(input("Введите сумму вклада: "))
# deposit = []
# for i in list(per_cent.values()):
#     deposit.append(float(money*i/100))
# deposit = [round(float(money * i / 100), 2) for i in list(per_cent.values())]
# print(deposit)
# print(max(deposit))

