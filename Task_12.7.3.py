per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму вклада: "))

deposit = []

for i in list(per_cent.values()):
    deposit.append(float(money*i/100))
deposit = [round(v, 2) for v in deposit]
print(deposit)

print(max(deposit))