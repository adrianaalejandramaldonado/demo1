"""def get_dates_in_interval(start_date, end_date):
    result = []
    if start_date is None or end_date is None:
        return
    if start_date == end_date:
        return [start_date]

    # TODO: Solve normal use case
    return result"""
from datetime import datetime
def get_dates_in_interval(start_date, end_date):
    dates = []

    if start_date != None or end_date != None:

        start_date_format_datetime = datetime.strptime(start_date, "%m/%d/%Y")
        end_date_format_datetime = datetime.strptime(end_date, "%m/%d/%Y")
        only_sd=start_date_format_datetime.date()
        only_ed=end_date_format_datetime.date()
        elapsed_date= only_ed.day - only_sd.day
        if only_sd.day>only_ed.day:
            return None
        for c in range(0,elapsed_date+1):
            date= f"{only_sd.month}/{only_sd.day+c}/{only_sd.year}"
            dates.append(date)
        return dates
    else:
        return None


def get_default_date_data(start_date, end_date, default_value):
    dates=[]
    dates_in_interval = get_dates_in_interval(start_date, end_date)
    if dates_in_interval != None:
        for date in dates_in_interval:
            obj = {}
            obj['date']=date
            obj['participants'] = default_value
            dates.append(obj)
    return dates