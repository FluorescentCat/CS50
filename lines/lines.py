import sys

def checkline():
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

elif len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
    try:
        with open(sys.argv[1], "r") as file:
            count = 0
            lines = file.readlines()
            for line in lines:
                if checkline() == False:
                    count += 1
            print(count)
    except FileNotFoundError:
        sys.exit(1)

else:
    sys.exit(1)