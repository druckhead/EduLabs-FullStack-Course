from os import listdir, makedirs
from os.path import join, exists
from csv import DictReader, DictWriter
from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait
from time import perf_counter_ns, perf_counter


# Date,Low,Open,Volume,High,Close,Adjusted Close


class CsvAvg:
    def __init__(self, fpath: str, delimiter: str = ','):
        if exists(fpath):
            self._fpath = fpath
        else:
            raise FileNotFoundError()
        self._delimiter = delimiter

        self._fieldnames = ["Date", "Low", "Open", "Volume", "High", "Close", "Adjusted Close"]

    def write_file(self, file_name, rows, hasheaders=True, mode="w"):
        with open(file_name, mode) as wh:
            writer = DictWriter(wh, fieldnames=self._fieldnames, delimiter=self._delimiter)
            if hasheaders:
                writer.writeheader()

            writer.writerows(rows)

    # load a file and return the contents
    def load_file(self, filepath):
        # open the file
        with open(filepath, 'r') as handle:
            # return the contents
            reader = DictReader(handle, delimiter=self._delimiter)
            rows = []
            for row in reader:
                rows.append(row)
        return rows

    # return the contents of many files
    def load_files(self, filepaths):
        # create a thread pool
        with ThreadPoolExecutor(16) as exe:
            # load files
            futures = [exe.submit(self.load_file, name) for name in filepaths]
            # collect data
            data_list = [future.result() for future in futures]
            # return data and file paths
            return (data_list, filepaths)

    def _calc_avg(self, data):
        avg_low = avg_open = avg_volume = avg_high = avg_close = avg_adj_close = 0.0
        num_rows = 0

        for row in data:
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

        return row_dict

    # load all files in a directory into memory
    def main(self, path='files'):
        # prepare all the paths
        paths = [join(path, filepath) for filepath in listdir(path)]
        # determine chunksize
        n_workers = 4
        chunksize = round(len(paths) / n_workers)
        # create the process pool
        with ProcessPoolExecutor(n_workers) as executor:
            futures = list()
            # split the load operations into chunks
            for i in range(0, len(paths), chunksize):
                # select a chunk of filenames
                filepaths = paths[i:(i + chunksize)]
                # submit the task
                future = executor.submit(self.load_files, filepaths)
                futures.append(future)
            # process all results
            with ThreadPoolExecutor(max_workers=4) as exe:
                pool = []
                for future in as_completed(futures):
                    # open the file and load the data
                    data_list, filepaths = future.result()
                    for filepath, data in zip(filepaths, data_list):
                        row_dict = self._calc_avg(data)
                        pool.append(exe.submit(self.write_file, filepath, [row_dict], hasheaders=False, mode='a'))
                        # self.write_file(filepath, [row_dict], hasheaders=False, mode='a')

    @staticmethod
    def _valid_dir():
        directory = 'files'
        if not exists(directory):
            makedirs(directory)
        return directory

    def sep_years(self):
        directory = self._valid_dir()
        prev_year = '1980'
        with open(self._fpath, 'r') as fh:
            reader = DictReader(fh, delimiter=self._delimiter)
            rows = []
            with ThreadPoolExecutor(max_workers=16) as exe:
                futures = []
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
                        path = join(directory, f"AAPL_{prev_year}.csv")
                        futures.append(exe.submit(self.write_file, path, rows[0:-1]))
                        # self.write_file(path, rows[0:-1])
                        rows = [rows[-1]]

                    prev_year = year
                path = join(directory, f"AAPL_{year}.csv")
                futures.append(exe.submit(self.write_file, path, rows))


if __name__ == '__main__':
    start = perf_counter()
    csvf = CsvAvg("/Users/danielraz/EduLabs-FullStack-Course/Lessons/Lesson_14/src/Homework/E5/AAPL.csv")
    csvf.sep_years()
    csvf.main("files")
    end = perf_counter()
    print(f"[Runtime: {end - start}s]")
