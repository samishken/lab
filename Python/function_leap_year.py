year = int(input("Enter Year: "))
def is_leap(year):
    leap = False

    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False
print(is_leap(year))