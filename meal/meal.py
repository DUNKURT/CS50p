def main():
    time = input('What time is it? ').strip().lower()
    if "am" in time or "pm" in time:
        hour_min, period = time.split(" ")
        hour, minute = map(int, hour_min.split(":"))

        # Convert to 24-hour format
        if period == "pm" and hour != 12:
            hour += 12
        elif period == "am" and hour == 12:
            hour = 0

        #print(f"24-hour format: {hour:02}:{minute:02}")
        
        time = str(hour) + ":" + str(minute)
        #print(time)
        eat = convert(time)
        if eat >= 7 and eat <=8:
                print("breakfast time")
        elif eat >= 12 and eat <=13:
                print("lunch time")
        elif eat >= 18 and eat <= 19:
                print("dinner time")
    else:
        eat = convert(time)
        if eat >= 7 and eat <=8:
                print("breakfast time")
        elif eat >= 12 and eat <=13:
                print("lunch time")
        elif eat >= 18 and eat <= 19:
                print("dinner time")
    
def convert(time):
    hour, min = time.split(":")
    hour = float(hour) + (float(min) / 60)
    return hour


if __name__ == "__main__":
    main()