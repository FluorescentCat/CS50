word = input("Input:")

for c in word:
    match c:
        case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
            c.replace(c, "")
        case _:
            print(c, end="")

