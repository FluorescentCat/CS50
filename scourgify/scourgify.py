import sys
import csv

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)

elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

elif len(sys.argv) == 3:
    if sys.argv[1].endswith(".csv"):
        try:
            students = []

            with open(sys.argv[1], "r") as csvfile1:
                reader = csv.DictReader(csvfile1)
                for row in reader:
                    last, first = row["name"].split(", ")
                    house = row["house"]
                    students.append({"first": first, "last": last, "house": house})

            with open(sys.argv[2], "w", newline='') as csvfile2:
                writer = csv. DictWriter(csvfile2, fieldnames=["first", "last", "house"])
                writer.writeheader()
                writer.writerows(students)


        except FileNotFoundError:
            sys.exit(1)
    else:
        print("Not a CSV file")
        sys.exit(1)