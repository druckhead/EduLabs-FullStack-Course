import os.path
import csv
from csv import DictReader, DictWriter
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, wait
from time import perf_counter_ns, perf_counter


# Date,Low,Open,Volume,High,Close,Adjusted Close


class CsvAvg:
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

    def write_file(self, file_name, rows, hasheaders=True, mode="w"):
        with open(file_name, mode) as wh:
            writer = DictWriter(wh, fieldnames=self._fieldnames, delimiter=self._delimiter)
            if hasheaders:
                writer.writeheader()

            writer.writerows(rows)

    def sep_years(self):
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
                    path = os.path.join(directory, f"AAPL_{prev_year}.csv")
                    self.write_file(f"{directory}/AAPL_{prev_year}.csv", rows[0:-1])
                    rows = [rows[-1]]

                prev_year = year
            path = os.path.join(directory, f"AAPL_{year}.csv")
            self.write_file(path, rows)

    def _calc_avg(self, directory, file):
        path = os.path.join(directory, file)

        with open(path, 'r') as fh:
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
        self.write_file(path, [row_dict], hasheaders=False, mode='a')

    def calc_avgs(self):
        directory = self._valid_dir()
        files = os.listdir(directory)
        for file in files:
            self._calc_avg(directory, file)


if __name__ == '__main__':
    start = perf_counter()
    csvf = CsvAvg("/Users/danielraz/EduLabs-FullStack-Course/Lessons/Lesson_14/src/Homework/E5/AAPL.csv")
    csvf.sep_years()
    tasks = csvf.calc_avgs()
    end = perf_counter()
    print(f"[Runtime: {end - start}s]")
