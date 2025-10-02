price = float(input('цена:'))
vat = float(input('ндс:'))
discount = float(input('скидка:'))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'после скидки:  {base:.2f}\nНДС: {vat_amount:.2f}\nитого: {total:.2f}')