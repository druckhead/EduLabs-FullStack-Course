import csv
from datetime import datetime


# Year,  Avg Price, Min Price, Max Price, Avg Volume, Min Volume, Max Volume

def get_year(date: str) -> int:
    date = datetime.strptime(date, "%d-%m-%Y").date()
    year = date.year
    return year


def create_new_csv_file(file_name: str, fieldnames: list[str]) -> None:
    with open(file_name, "w") as new_file:
        writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=",", quoting=csv.QUOTE_NONE)
        writer.writeheader()


def write_to_file(file_name: str, fieldnames: list[str], row_dict: dict[str, int | float]) -> None:
    with open(file_name, "a") as new_file:
        writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=",", quoting=csv.QUOTE_NONE)
        writer.writerow(row_dict)


def create_row_dict(year: int, avg_price: float, min_price: float, max_price: float, avg_volume: float,
                    min_volume: float, max_volume: float) -> dict[str, int | float]:
    return {
        "Year": year,
        "Avg Price": avg_price,
        "Min Price": min_price,
        "Max Price": max_price,
        "Avg Volume": avg_volume,
        "Min Volume": min_volume,
        "Max Volume": max_volume,
    }


def update_file(file_name: str, from_file: str, fieldnames: list[str]) -> None:
    avg_price, min_price, max_price = 0.0, float('inf'), -float('inf')
    avg_volume, min_volume, max_volume = 0.0, float('inf'), -float('inf')
    total_volume: float = 0
    total_price: float = 0
    prev_year: int = 0
    row_cntr: int = 0

    with open(from_file, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",", quoting=csv.QUOTE_NONE)

        for row in reader:
            date: str = row["Date"]
            curr_year: int = get_year(date)

            if 0 != prev_year != curr_year:
                row_dict = create_row_dict(prev_year,
                                           total_price / row_cntr,
                                           min_price, max_price,
                                           total_volume / row_cntr,
                                           min_volume,
                                           max_volume)

                avg_price, min_price, max_price = 0.0, float('inf'), -float('inf')
                avg_volume, min_volume, max_volume = 0.0, float('inf'), -float('inf')
                row_cntr = 0
                total_price = 0
                total_volume = 0

                write_to_file(file_name, fieldnames, row_dict)

            # calculate values
            min_price = min(min_price, float(row["Low"]))
            max_price = max(max_price, float(row["High"]))
            min_volume = min(min_volume, float(row["Volume"]))
            max_volume = max(max_volume, float(row["Volume"]))
            total_volume += float(row["Volume"])
            total_price += ((float(row["Low"]) + float(row["High"])) / 2)
            row_cntr += 1

            prev_year = curr_year

    # to get the missing final year
    row_dict = create_row_dict(prev_year,
                               total_price / row_cntr,
                               min_price,
                               max_price,
                               total_volume / row_cntr,
                               min_volume,
                               max_volume)

    write_to_file(file_name, fieldnames, row_dict)


def apple_stock_csv(fpath: str, new_file_name: str):
    fieldnames = ['Year', 'Avg Price', 'Min Price', "Max Price", 'Avg Volume', "Min Volume", 'Max Volume']
    create_new_csv_file(new_file_name, fieldnames)
    update_file(new_file_name, fpath, fieldnames)


if __name__ == "__main__":
    # create a new csv of AAPL stock avgs
    apple_stock_csv("/Users/danielraz/EduLabs-FullStack-Course/Lessons/Lesson_9/src/Lesson_Code/files/data/AAPL.csv",
                    "avg_aapl_prices.csv")

    # test out the file we created
    with open("avg_aapl_prices.csv", 'r') as f:
        csvreader = csv.reader(f, delimiter=",", quoting=csv.QUOTE_NONE)
        for _row in csvreader:
            print(_row)
