'''
Every year that is exactly divisible by four is a leap year,
except for years that are exactly divisible by 100,
but these centurial years are leap years if they are exactly divisible by 400.
For example, the years 1700, 1800, and 1900 are not leap years,
but the years 1600 and 2000 are.
'''


def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
    elif year % 4 == 0 and (year % 100) == 0:
        leap = False
    else:
        leap = False

    if leap:
        print("is a leap yr")
    else:
        print("is not a leap yr")

    return leap


year = int(input("Enter year: "))
is_leap(year)
