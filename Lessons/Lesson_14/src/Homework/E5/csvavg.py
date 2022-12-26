import os.path
import csv
from csv import DictReader, DictWriter
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter


# Date,Low,Open,Volume,High,Close,Adjusted Close


class CsvAvg:
    # fieldnames = ["Avg Low", "Min Open", "Avg Volume", "Avg High", "Avg Close", "Avg Adjusted Close"]

    def __init__(self, fpath: str, delimiter: str = ','):
        if os.path.exists(fpath):
            self._fpath = fpath
        else:
            raise FileNotFoundError()
        self._delimiter = delimiter

        self._fieldnames = ["Date", "Low", "Open", "Volume", "High", "Close", "Adjusted Close"]

    @staticmethod
    def _valid_dir():
        directory = 'files'
        if not os.path.exists(directory):
            os.makedirs(directory)
        return directory

    def a(self):
        directory = self._valid_dir()

        prev_year = '1980'
        with open(self._fpath, 'r') as fh:
            reader = DictReader(fh, delimiter=self._delimiter)
            rows = []
            for row in reader:
                year = row["Date"][6:]

                rows.append({
                    "Date": row["Date"],
                    "Low": row["Low"],
                    "Open": row["Open"],
                    "Volume": row["Volume"],
                    "High": row["High"],
                    "Close": row["Close"],
                    "Adjusted Close": row["Adjusted Close"],
                })

                if year != prev_year:
                    with open(f"{directory}/AAPL_{prev_year}.csv", 'w') as wh:
                        writer = DictWriter(wh, fieldnames=self._fieldnames, delimiter=self._delimiter)
                        writer.writeheader()

                        writer.writerows(rows[0:-1])
                        rows = [rows[-1]]

                prev_year = year

            with open(f"{directory}/AAPL_{year}.csv", 'w') as wh:
                writer = DictWriter(wh, fieldnames=self._fieldnames, delimiter=self._delimiter)
                writer.writeheader()

                writer.writerows(rows[0:-1])

    def calc_avg(self):
        # Date, Low, Open, Volume, High, Close, Adjusted Close

        directory = self._valid_dir()

        files = os.listdir(directory)
        for file in files:
            with open(f"{directory}/{file}", 'r') as fh:
                reader = DictReader(fh, delimiter=self._delimiter)

                avg_low = avg_open = avg_volume = avg_high = avg_close = avg_adj_close = 0.0
                num_rows = 0

                for row in reader:
                    avg_low += float(row["Low"])
                    avg_open += float(row["Open"])
                    avg_volume += float(row["Volume"])
                    avg_high += float(row["High"])
                    avg_close += float(row["Close"])
                    avg_adj_close += float(row["Adjusted Close"])
                    num_rows += 1

                row_dict = {
                    "Date": '',
                    "Low": avg_low / num_rows,
                    "Open": avg_open / num_rows,
                    "Volume": avg_volume / num_rows,
                    "High": avg_high / num_rows,
                    "Close": avg_close / num_rows,
                    "Adjusted Close": avg_adj_close / num_rows,
                }

                with open(f"{directory}/{file}", 'a') as wh:
                    writer = DictWriter(wh, fieldnames=self._fieldnames, delimiter=self._delimiter)
                    writer.writerow(row_dict)


if __name__ == '__main__':
    csvf = CsvAvg("/Users/danielraz/EduLabs-FullStack-Course/Lessons/Lesson_14/src/Homework/E5/AAPL.csv")
    start = perf_counter()
    csvf.a()
    csvf.calc_avg()
    end = perf_counter()
    print(f"[Runtime: {end - start}s]")
