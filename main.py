tickets = int(input("Enter the number of tickets you want to purchase: "))
total_cost = 0

for i in range(tickets):
    age = int(input("Enter the age of the visitor: "))
    if age < 18:
        cost = 0
    elif age < 25:
        cost = 990
    else:
        cost = 1390
    total_cost += cost

if tickets > 3:
    total_cost = total_cost - (total_cost * 0.1)

print("Total cost:", total_cost)
