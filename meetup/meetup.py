import datetime as dt
import calendar


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):
    # Define dictionary of Weekdays to match response given weekday() datetime method
    days_dict = {0: 'Monday',
                 1: 'Tuesday',
                 2: 'Wednesday',
                 3: 'Thursday',
                 4: 'Friday',
                 5: 'Saturday',
                 6: 'Sunday'}

    last_day = calendar.monthrange(year, month)[1]
    first_dom = calendar.monthrange(year, month)[0]
    days = [x for x in range(1, last_day + 1)]
    days_detail = {}
    for day in days:
        days_detail[day] = days_dict[dt.datetime(year, month, day).weekday()]
    selections = [x for x in days_detail.items() if x[1] == day_of_week]
    # Handle various description cases
    if week == 'teenth':
        for selection in selections:
            if selection[0] >= 13 and selection[0] <= 19:
                return dt.date(year, month, selection[0])
    elif week == 'last':
        return dt.date(year, month, max(selections)[0])
    else:
        # Try to return valid entry from possible selections, otherwise raise Exception
        try:
            return dt.date(year, month, selections[int(week[0]) - 1][0])
        except IndexError as e:
            raise MeetupDayException("Invalid calendar entry.")
