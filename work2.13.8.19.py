number_of_tickets = int(input("Сколько билетов хотите приобрести? "))
print("Укажите возраст каждого посетителя ")
s = 0
for i in range(number_of_tickets):
    age = int(input("Возраст: "))
    if age < 18:
        s += 0
    elif 18 <= age < 25:
        s += 990
    else:
        s += 1390
if number_of_tickets > 3:
    f = 0.9
else:
    f = 1
print("Сумма к оплате -" , s * f)