def valueinput():
    x, y = input("Fraction: ").split("/")
    x = int(x)
    y = int(y)
    return x, y

def main():
    try:
        x, y = valueinput()
        if x > y:
            valueinput()
        fraction = round(x / y * 100)
        if fraction <= 1:
            print("E")
        elif fraction >= 99:
            print("F")
        else:
            print(f"{fraction:.0f}" + "%")
    except ValueError:
        valueinput()
    except ZeroDivisionError:
        valueinput()

main()