def weekDay(date_day):
    """

    :param date_day: a date in datetime format (yyyy-mm-dd)
    :return:
    """
    year, month, day = date_day.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week = ['Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday']
    afterFeb = 1
    if month > 2:
        afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    day_of_week = 5
    # partial sum of days betweem current date and 1700/1/1
    day_of_week += (aux + afterFeb) * 365
    # leap year correction
    day_of_week += aux / 4 - aux / 100 + (aux + 100) / 400
    # sum monthly and day offsets
    day_of_week += offset[month - 1] + (day - 1)
    day_of_week %= 7
    day_of_week = int(day_of_week)
    return week[day_of_week]