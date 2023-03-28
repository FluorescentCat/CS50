def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError()
    if x > y:
        raise ValueError()
    intfraction = round(x / y * 100)
    return intfraction

def gauge(percentage):
    result = ""
    if percentage <= 1:
        result = "E"
    elif percentage >= 99:
        result = "F"
    else:
        result = str(percentage) + "%"
    return result

def main():
        fraction = input("Fraction: ")
        intfraction = convert(fraction)
        result = gauge(intfraction)
        print(result)




if __name__ == "__main__":
    main()