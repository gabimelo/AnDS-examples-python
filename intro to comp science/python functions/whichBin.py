"""@param: d, m, y in format D/M/YYYY
@pre: isLeapYear is defined, date_difference is defined
@post: returns which bin you should put out next monday
@complexity: O(Y)"""
def whichBin(d, m, y):
        import math
        
        if ( (y > 2014) or (y == 2014 and (m>3 or (m==3 and d>=10)))):
                days = date_difference(d, m, y, 10, 3, 2014)
        else:
                days = date_difference(10, 3, 2014, d, m, y)

        if math.floor(days/7) % 2 == 0:
                return("green")
        else:
                return("yellow")