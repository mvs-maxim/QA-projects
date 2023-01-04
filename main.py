per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада: "))

TKB = round(money * (per_cent.get('ТКБ')/100))
SKB = round(money * (per_cent.get('СКБ')/100))
VTB = round(money * (per_cent.get('ВТБ')/100))
SBER = round(money * (per_cent.get('СБЕР')/100))
deposit = [TKB, SKB, VTB, SBER]

print("Максимальная сумма, которую вы можете заработать — ", max(deposit))
