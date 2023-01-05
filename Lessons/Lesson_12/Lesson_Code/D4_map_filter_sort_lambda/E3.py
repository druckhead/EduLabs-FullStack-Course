from datetime import datetime


def filter_weekdays(dates: list[str]) -> list[str]:
    strftime = datetime.strftime
    return list(
        map(
            lambda date: datetime.strftime(date, "%d-%m-%Y"),
            filter(
                lambda is_day: strftime(is_day, "%A") == "Saturday" or strftime(is_day, "%A") == "Friday",
                map(
                    lambda date_str: datetime.strptime(date_str, "%d-%m-%Y").date(),
                    dates
                )
            )
        )
    )


if __name__ == '__main__':
    print(filter_weekdays(["12-12-2021", "16-12-2021", "17-12-2021", "18-12-2021", "19-12-2021"]))
