answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = str.lower(answer).lstrip().rstrip()

if answer == "42":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer == "forty two":
    print("Yes")
else:
    print("No")