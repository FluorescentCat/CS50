import random

def main():
    level = get_level()
    questions = 0
    fails = 0
    score = 0
    while questions < 10:
        questions += 1
        fails = 0
        x, y = generate_integer(level)
        answer = x + y
        while fails < 3:
            user_answer = int(input(f"{x} + {y} = "))
            if answer == user_answer:
                score += 1
                break
            else:
                fails += 1
                print("EEE")
                continue
        else:
           print(f"{x} + {y} = {answer}")
           continue
    print(score)



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level ==3:
                break
            else:
                continue
        except ValueError:
            continue
        except EOFError:
            break
    return level

def generate_integer(level):
    if level == 3:
        x = random.randrange(100, 1000, 1)
        y = random.randrange(100, 1000, 1)
    elif level == 2:
        x = random.randrange(10, 100, 1)
        y = random.randrange(10, 100, 1)
    else:
        x = random.randrange(0, 10, 1)
        y = random.randrange(0, 10, 1)
    return x, y



if __name__ == "__main__":
    main()