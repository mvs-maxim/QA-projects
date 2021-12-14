price_all = 0
age_for_ticket = []
ticket_number = input('Сколько билетов вы хотите приобрести на мероприятие? ')
ticket_number = int(ticket_number)
for number in range(0, ticket_number):
    for_ticket = int(input('Укажите возраст: '))
    age_for_ticket.append(for_ticket)
for i in age_for_ticket:
    if i < 18:
            print('Билет бесплатный')
    elif 25 > i >= 18:
            price_all += 990
            print('Стоимость билета: 990 руб.')
    else:
            price_all += 1390
            print('Стоимость билета: 1390 руб.')
if ticket_number > 3:
    price_all *= 0.9
    print(f'Сумма к оплате {price_all} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше 3-и человек')
else:
    print(f'Сумма к оплате {price_all} руб.')