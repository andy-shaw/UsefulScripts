
def workdays(month, year):
    '''calculate the weekdays of a month and year ('jan', 2015), ('dec', 2018), ...'''
    import datetime
    months = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'april': 4,
        'may': 5,
        'june': 6,
        'july': 7,
        'aug': 8,
        'sept': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }

    month = months[month.lower()]
    next_month = (month + 1) % (len(months.keys()) + 1)
    year = int(year)
    if month > next_month: 
        next_year = int(year) + 1
    else:
        next_year = year

    fromdate = datetime.date(year,month,1)
    todate = datetime.date(next_year,next_month,1)
    daygenerator = (fromdate + datetime.timedelta(x + 1) for x in xrange((todate - fromdate).days))
    return sum(1 for day in daygenerator if day.weekday() < 5)

def daysinmonth(day, month, year):
    '''calculate how many occurances of the day of the week happen in the month ('sat' -> 4)'''
    import datetime
    months = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'april': 4,
        'may': 5,
        'june': 6,
        'july': 7,
        'aug': 8,
        'sept': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }
    days = {
        'mon' : 0,
        'tues' : 1,
        'wed' : 2,
        'thur' : 3,
        'fri' : 4,
        'sat' : 5,
        'sun' : 6
    }

    day = days[day.lower()]
    month = months[month.lower()]
    next_month = (month + 1) % (len(months.keys()) + 1)
    year = int(year)
    if month > next_month: 
        next_year = int(year) + 1
    else:
        next_year = year

    fromdate = datetime.date(year,month,1)
    todate = datetime.date(next_year,next_month,1)
    daygenerator = (fromdate + datetime.timedelta(x + 1) for x in xrange((todate - fromdate).days))
    return sum(1 for day in daygenerator if day.weekday() = day)