"""@param: d, m, y in format D/M/YYYY
@pre: isLeapYear is defined, d, m, y is a later date than d1, m1, y1
@post: returns amount of days in between 2 dates passed as parameters
@complexity: O(Y)"""
def date_difference(d, m, y, d1, m1, y1):
        import isLeapYear
        days = 0
        
        while d != d1:
                days += 1
                d -= 1
                if d==0:
                        if m==2 or m==4 or m==6 or m==8 or m==9 or m==11 or m==1:
                                d = 31
                        elif m == 3:
                                if isLeapYear.isLeapYear(y):
                                        d = 29
                                else:
                                        d = 28
                        else:
                                d = 30
                        m -= 1
                                
        while m != m1:
                if m==2 or m==4 or m==6 or m==8 or m==9 or m==11 or m==1:
                        days += 31
                elif m == 3:
                        if isLeapYear.isLeapYear(y):
                                days += 29
                        else:
                                days += 28
                else:
                        days += 30
                m -= 1
                if m == 0:
                        m = 12
                        y -= 1

        while y != y1:
                if isLeapYear.isLeapYear(y):
                        days += 366
                else:
                        days += 365
                y -= 1

        return days

print(date_difference(1, 3, 2016, 22, 11, 2014))