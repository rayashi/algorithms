from datetime import datetime, timezone


def datetime_difference(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    first = datetime.strptime(t1, fmt)
    second = datetime.strptime(t2, fmt)
    return str(int(abs((first - second).total_seconds())))
