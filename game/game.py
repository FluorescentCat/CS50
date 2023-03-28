import random

while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            continue
        else:
            break
    except ValueError:
        continue
    except EOFError:
        break

ranlevel = random.randint(1, level)
#print(ranlevel)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < ranlevel:
            print("Too small!")
            continue
        elif guess > ranlevel:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break
    except ValueError:
        continue
    except EOFError:
        break