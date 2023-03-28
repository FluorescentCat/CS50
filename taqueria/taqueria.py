

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


cost = 0
while True:
    try:
        food = input("Item: ").title()
        for x in menu:
            if food == x:
                price = menu.get(food)
                cost = cost + price
                print("Total: $" + f"{cost:.2f}")
            else:
                continue
    except EOFError:
        print("\n" "Total: $" + f"{cost:.2f}")
        break
    except KeyError:
        continue


