import re
import sys


def main():
    ip = input("IPv4 Address: ").strip()
    validate(ip)



def validate(ip):
    if re.search(r"^\d   $", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
