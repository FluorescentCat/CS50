inputname = input("give name in camelCase: ")


for c in inputname:
    if c.islower():
        print(c, end="")
    else:
        c = c.lower()
        print("_" + c, end="")
