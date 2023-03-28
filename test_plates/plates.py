def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if checklength(s):
        if checkalphanum(s):
            if checkfirsttwo(s):
                if checkzero(s):
                    if checklastdigit(s):
                        return True
                    else:
                        return False

def checklength(s):
    length = len(s)
    if length >= 2 and length <= 6:
        return True
    else:
        return False

def checkalphanum(s):
    if s.isalnum():
        return True
    else:
        return False

def checkfirsttwo(s):
    firsttwo = s[0:2]
    if firsttwo.isalpha():
        return True
    else:
        return False

def checkzero(s):
    if "0" in s:
        zeroIndex = s.find("0") - 1
        if s[-(zeroIndex)].isdigit():
            for c in s:
                if c.isdigit():
                    if c.startswith('0'):
                        return False
                    else:
                        return True
    else:
        return True

def checklastdigit(s):
    if s[-2].isdigit() and s[-1].isalpha():
        return False
    elif s[-2].isdigit():
        return True
    elif s.isalpha():
        return True


if __name__ == "__main__":
    main()


