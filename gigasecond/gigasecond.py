import datetime as dt


def add(birth_date):
    """return the given date plus 10^9 seconds"""
    delta = 10**9
    final_date = birth_date + dt.timedelta(0, delta)
    return final_date


birth_date = dt.datetime(1989, 8, 3)
print(add(birth_date))
