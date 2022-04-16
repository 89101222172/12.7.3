money = float(input('Введите сумму вклада (рублей):'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
banks = list(per_cent.keys())
per_cent = list(per_cent.values())
deposit = list()
deposit.append(int(money / 100 * float(per_cent[0])))
deposit.append(int(money / 100 * float(per_cent[1])))
deposit.append(int(money / 100 * float(per_cent[2])))
deposit.append(int(money / 100 * float(per_cent[3])))
print(f'\nДоход по депозиту составит:\n{banks[0]} банк - {deposit[0]} рублей\n{banks[1]} банк - {deposit[1]} ' 
f'рублей\n{banks[2]} банк - {deposit[2]} рублей\n{banks[3]} банк - {deposit[3]}рублей\n')
# Максимальная сумма которую можно заработать
max_deposit = max(deposit)
print('Максимальная сумма которую Вы можете заработаеть: {} рублей.'.format(max_deposit))