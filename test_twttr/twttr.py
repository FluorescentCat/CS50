def main():
    word = input("Input:")
    shortword = shorten(word)
    print(shortword)
    #print("\n")

def shorten(word):
    shortword = ""
    for c in word:
        match c:
            case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
                c = c.replace(c, "")
        shortword += c
    return shortword
            #case _:
                #print(c, end="")

if __name__ == "__main__":
    main()