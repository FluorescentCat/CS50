def main():
    money = 0
    greeting = input("Please type a greeting here: ").lower()
    value(greeting)
    print(f"${money}")

def value(greeting):
    if greeting.startswith("hello") or greeting.startswith("Hello"):
        money = 0
    elif greeting.startswith("h") or greeting.startswith("H") and not greeting.startswith("hello"):
        money = 20
    else:
        money = 100
    return money

if __name__ == "__main__":
    main()