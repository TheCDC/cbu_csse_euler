def days_in_month(month, year):
    # September, April, June, Novemeber    
    if month in [9, 4, 6, 11]:
        return 30
    # February
    if month == 2:
        if year % 4 == 0 and year % 400 != 0:
            return 29
        else:
            return 28
    # All the rest    
    else:
        return 31

def main():
    # 1900 was a leap year    
    day = 366
    sundays = 0
    # Iterate over the years
    for year in range(1901, 2001):
        # Iterate over the months
        for month in range(1, 13):
            # Sunday is the 7th day in our counters
            if day % 7 == 0:
                sundays += 1
            day += days_in_month(month, year)

    print(sundays)


if __name__ == "__main__":
    main()
