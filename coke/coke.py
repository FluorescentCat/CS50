
amountdue = 50

while amountdue > 0:
    coin = int(input("Insert coin: "))
    match coin:
        case 5 | 10 | 25:
            amountdue = amountdue - coin
            if amountdue <= 0:
                amountdue = abs(amountdue)
                print("Change Owed:", amountdue)
                break
            print("Amount Due:", amountdue)
        case _:
            print("Amount Due:", amountdue)




