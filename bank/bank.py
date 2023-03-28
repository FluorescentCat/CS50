greeting = input("Please type a greeting here: ").strip()


if greeting.startswith("Hello") or greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("H") and not greeting.startswith("Hello"):
    print("$20")
elif greeting.startswith("h") and not greeting.startswith("hello"):
    print("$20")
else:
    print("$100")