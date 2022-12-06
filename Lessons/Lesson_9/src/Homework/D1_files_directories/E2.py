import csv
from datetime import datetime


# Year,  Avg Price, Min Price, Max Price, Avg Volume, Min Volume, Max Volume

def get_year(date: str) -> int:
    date = datetime.strptime(date, "%d-%m-%Y").date()
    year = date.year
    return year


def apple_stock_csv(fpath: str):
    fieldnames = ['Year', 'Avg Price', 'Min Price', "Max Price", 'Avg Volume', "Min Volume",
                  'Max Volume']
    with open("avg_aapl_prices.csv", "w") as new_file:
        writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=",", quoting=csv.QUOTE_NONE)
        writer.writeheader()

    prev_year: int = 0
    row_cntr: int = 0
    avg_price, min_price, max_price, avg_volume, min_volume, max_volume = 0.0, float('inf'), -float('inf'), 0.0, float(
        'inf'), -float('inf')
    total_volume: float = 0
    total_price: float = 0

    with open(fpath, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",", quoting=csv.QUOTE_NONE)
        for row in reader:
            date: str = row["Date"]
            curr_year: int = get_year(date)

            if 0 != prev_year != curr_year:
                # todo create dict and write to new file
                row_dict = {
                    "Year": prev_year,
                    "Avg Price": total_price / row_cntr,
                    "Min Price": min_price,
                    "Max Price": max_price,
                    "Avg Volume": total_volume / row_cntr,
                "Min Volume": min_volume,
                "Max Volume": max_volume,
                }
                avg_price, min_price, max_price, avg_volume, min_volume, max_volume = 0.0, float('inf'), -float(
                    'inf'), 0.0, float('inf'), -float('inf')
                row_cntr = 0
                total_price = 0
                total_volume = 0

                with open("avg_aapl_prices.csv", "a") as new_file:
                    writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=",", quoting=csv.QUOTE_NONE)
                    writer.writerow(row_dict)

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
        row_dict = {
            "Year": prev_year,
            "Avg Price": total_price / row_cntr,
            "Min Price": min_price,
            "Max Price": max_price,
            "Avg Volume": total_volume / row_cntr,
            "Min Volume": min_volume,
            "Max Volume": max_volume,
        }

        with open("avg_aapl_prices.csv", "a") as new_file:
            writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=",", quoting=csv.QUOTE_NONE)
            writer.writerow(row_dict)


if __name__ == "__main__":
    apple_stock_csv("/Users/danielraz/EduLabs-FullStack-Course/Lessons/Lesson_9/src/Lesson_Code/files/data/AAPL.csv")
    with open("avg_aapl_prices.csv", 'r') as f:
        field_names = ['Year', 'Avg Price', 'Min Price', "Max Price", 'Avg Volume', "Min Volume",
                      'Max Volume']
        csvreader = csv.reader(f, delimiter=",", quoting=csv.QUOTE_NONE)
        for _row in csvreader:
            print(_row)
