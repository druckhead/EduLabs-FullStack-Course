from datetime import date, timedelta


def dateiterator(__date: date):
    """
    create a date iterator starting from __date until the end of the month\n
    :param __date:
    :return:
    """
    start_month = __date.month
    while start_month == __date.month:
        curr_date = __date
        __date += timedelta(days=1)
        yield curr_date


if __name__ == '__main__':
    dt = dateiterator(date(2022, 3, 26))
    for d in dt:
        print(d)
