def calendar(m, y):
    print("\n")
    if ((y > 2014) or (y == 2014 and m > 3)):
        days = date_difference(1, m, y, 9, 3, 2014)
    else:
        days = date_difference(9, 3, 2014, 1, m, y)
    offset = days % 7

    if m == 1:
        print("January - ", end = "")
        maxday = 31
    elif m == 2:
        print("February - ", end = "")
        if isLeapYear(y):
            maxday = 29
        else:
            maxday = 28
    elif m == 3:
        print("March - ", end = "")
        maxday = 31
    elif m == 4:
        print("April - ", end = "")
        maxday = 30
    elif m == 5:
        print("May - ", end = "")
        maxday = 31
    elif m == 6:
        print("June - ", end = "")
        maxday = 30
    elif m == 7:
        print("July - ", end = "")
        maxday = 31
    elif m == 8:
        print("August - ", end = "")
        maxday = 31
    elif m == 9:
        print("September - ", end = "")
        maxday = 30
    elif m == 10:
        print("October - ", end = "")
        maxday = 31
    elif m == 11:
        print("November - ", end = "")
        maxday = 30
    else:
        print("December - ", end = "")
        maxday = 31
        
    print(y)
    print("\n")

    print("| Sun || Mon || Tue || Wed || Thu || Fri || Sat |" )
    print("\n")
    for _ in range(offset):
        print("|     |", end = "")

    pos = offset

    day = 1

    while (day <= maxday):
        if (day < 10):
            print("|  " + str(day) +  "  |", end = "")
        else:
            print("| " + str(day) +  "  |", end = "")
        pos += 1
        if (pos == 7):
            print("\n")
            pos = 0
        day += 1