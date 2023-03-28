months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def dateinput():
    date = input("Date: ").title()
    return date



while True:
    date = dateinput()
    try:
        month, day, year = date.replace(",", "").split("/")
        month = int(month)
        day = int(day)
        year = int(year)
        if (month >= 1 and month <= 12 and day >= 1 and day <= 31):
            break

    except:
        try:
            month, day, year = date.split(" ")
            if not day.endswith(","):
                continue
            day = day.replace(",", "")
            if month.isnumeric():
                month = int(month)
            elif month.isalpha():
                    month = months.index(month) + 1
            month = int(month)
            day = int(day)
            year = int(year)

            if (month >= 1 and month <= 12 and day >= 1 and day <= 31):
                break
        except:
            print()

print(f"{year}-{month:02}-{day:02}")


