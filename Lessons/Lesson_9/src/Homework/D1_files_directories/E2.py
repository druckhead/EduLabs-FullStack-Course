import csv
from datetime import datetime

# Year,  Avg Price, Min Price, Max Price, Avg Volume, Min Volume, Max Volume

def get_year(date: str) -> int:
    date = datetime.strptime(date, "%d-%m-%Y").date()
    year = date.year
    return year

def apple_stock_csv(fpath: str):
    with open(fpath, 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            fdate = row["Date"]
            year = get_year(fdate)






if __name__ == "__main__":
    apple_stock_csv("/Users/danielraz/EduLabs-FullStack-Course/Lessons/Lesson_9/src/Lesson_Code/files/data/AAPL.csv")
