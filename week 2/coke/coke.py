amountdue = 50

while amountdue > 0 :
    print('Amount Due:', amountdue)
    payedamount = int(input('Insert Coin: '))
    if payedamount in [5, 10 ,25]:
        amountdue -= payedamount

changeowed = abs(amountdue)
print("Change Owed:", changeowed)