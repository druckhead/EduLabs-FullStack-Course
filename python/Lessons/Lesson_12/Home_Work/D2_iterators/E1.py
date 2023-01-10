# Implement a simple class DateIterator that should be initialized with a date and
# implements iterator protocol (__iter__ and __next__ method)  that on every iteration
# returns the next date up until the end of the month.
from datetime import date, timedelta


class DateIterator:
    def __init__(self, curr_date: date):
        self._curr_date = curr_date

    def __iter__(self):
        self.__day = self._curr_date.day
        self.__month = self._curr_date.month
        return self

    def __next__(self):
        if self._curr_date.month != self.__month:
            raise StopIteration()
        curr_date = self._curr_date
        self._curr_date += timedelta(days=1)
        return curr_date


if __name__ == '__main__':
    dt = date(year=2013, month=2, day=1)
    di = DateIterator(dt)
    for day in di:
        print(day)
