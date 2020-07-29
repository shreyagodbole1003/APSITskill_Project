#To check if the given year is a leap year.
def test_year(year): 
    if (year % 4) == 0: 
        if (year % 100) != 0: 
            if (year % 400) == 0: 
                return True
            else: 
                return True
        else: 
             return True
    else: 
        return False
