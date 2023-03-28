import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

elif len(sys.argv) == 2:
    if sys.argv[1].endswith(".csv"):
        try:
            with open(sys.argv[1], "r") as csvfile:
                reader = csv.reader(csvfile)
                table = tabulate(reader, headers="firstrow", tablefmt="grid")
                print(table)
        except FileNotFoundError:
            sys.exit(1)
    else:
        print("Not a CSV file")
        sys.exit(1)

