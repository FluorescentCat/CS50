def main():
    time = input("What time is it? ")
    time = convert(time)
    #print(decimaltime)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)
    minute = minute / 60
    time = hour + minute
    return time
    #seconds = hour * 3600 + minute * 60
    #return seconds

if __name__ == "__main__":
    main()
