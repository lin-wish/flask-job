import datetime
import timeago

def compute_ago(created_time):
    date = datetime.datetime.fromtimestamp(int(float(str(created_time))))
    now = datetime.datetime.now()
    return timeago.format(date, now)
