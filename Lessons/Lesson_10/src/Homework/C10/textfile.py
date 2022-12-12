import csv
from csv import DictWriter, DictReader
import json
import os.path
from abc import ABC, abstractmethod
from typing import TextIO, Any
from customexceptions import *


class TextFile(ABC):
    def __init__(self, fpath: str):
        if not os.path.exists(fpath):
            raise FileNotFoundError
        if os.path.splitext(fpath)[-1] != self._get_ext():
            raise InvalidFileExtension

        self._fpath = fpath

    def get_file_size(self):
        """
        returns file size in bytes
        :return:
        """
        return os.path.getsize(self._fpath)

    def get_file_content(self):
        with open(self._fpath, 'r') as fh:
            content = self._get_specific_content(fh)
        return content

    def _validate_concat_path(self, other):
        if not isinstance(other, type(self)):
            raise Exception(f"{other} is not a {self._get_ext()} file")

        abspath = os.path.abspath(self._fpath)
        newfile_path = '_'.join([os.path.splitext(abspath)[0], os.path.abspath(other._fpath).split('/')[-1]])

        if os.path.exists(newfile_path):
            raise FileExistsError

        return newfile_path

    @abstractmethod
    def _get_specific_content(self, fh: TextIO):
        pass

    @abstractmethod
    def _get_ext(self):
        pass


class CsvFile(TextFile):
    def __init__(self, fpath: str, delimiter: str = ','):
        super().__init__(fpath)

        self._delimiter = delimiter

    def _get_ext(self):
        return ".csv"

    def _get_delimiter(self):
        return self._delimiter

    def _get_specific_content(self, fh: TextIO) -> list[dict[str | Any]]:
        content: list[dict[str | Any]] = []

        reader = DictReader(fh, delimiter=self._delimiter)
        for row in reader:
            content.append(row)

        return content

    def _append_to_file(self, ls: list, fh: TextIO):
        reader = DictReader(fh, delimiter=self._delimiter)
        fieldnames = reader.fieldnames
        for row in reader:
            rowdict = {}
            for fn in fieldnames:
                rowdict[fn] = row[fn]
            ls.append(rowdict)

    def get_num_rows(self):
        jsonfile = self.get_file_content()
        return len(jsonfile)

    def get_num_cols(self):
        jsonfile: list[dict[str, int | float]] = self.get_file_content()
        if self.get_num_rows() == 0:
            return 0

        return len(jsonfile[-1].keys())

    def get_row(self, row_num: int):
        if row_num < 1 or row_num > self.get_num_rows() + 1:
            raise IndexError()

        with open(self._fpath, 'r') as csvfile:
            reader = DictReader(csvfile, delimiter=self._delimiter)
            fieldnames = reader.fieldnames

            if fieldnames and all([name.replace(" ", "").isalpha() for name in fieldnames]):
                ret_val = self.get_file_content()[row_num - 1]
            else:
                if row_num == 1:
                    ret_val = {ind: fieldnames[ind - 1] for ind in range(1, self.get_num_cols() + 1)}
                else:
                    ret_val = {ind: self.get_file_content()[row_num - 2][fieldnames[ind - 1]] for ind in
                               range(1, self.get_num_cols() + 1)}

        return ret_val

    def get_col(self, col: int):
        if col < 1 or col > self.get_num_cols():
            raise IndexError()
        ret_val: list = []

        with open(self._fpath, 'r') as csvfile:
            reader = DictReader(csvfile, delimiter=self._delimiter)
            fieldnames = reader.fieldnames

            for row in reader:
                ret_val.append(row[fieldnames[col - 1]])

        return ret_val

    def get_cell(self, row: int, col: int):
        if row < 1 or row > self.get_num_rows():
            raise IndexError()
        if col < 1 or col > self.get_num_cols():
            raise IndexError()

        with open(self._fpath, 'r') as csvfile:
            reader = DictReader(csvfile, delimiter=self._delimiter)
            fieldnames = reader.fieldnames

        curr_row = self.get_row(row)
        ret_val = curr_row.get(fieldnames[col - 1])

        return ret_val

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise Exception(f"{other} is not a {self._get_ext()} file")

        newfile_name = self._validate_concat_path(other)

        with open(self._fpath, 'r') as lhs:
            lhs_reader = DictReader(lhs, delimiter=self._delimiter)
            lhs_fieldnames = lhs_reader.fieldnames

        with open(other._fpath, 'r') as rhs:
            rhs_reader = DictReader(rhs, delimiter=other._delimiter)
            rhs_fieldnames = rhs_reader.fieldnames

        if set(lhs_fieldnames) != set(rhs_fieldnames):
            raise Exception

        new_content = []

        with open(self._fpath, 'r') as lhs:
            self._append_to_file(new_content, lhs)

        with open(other._fpath, 'r') as rhs:
            self._append_to_file(new_content, rhs)

        with open(newfile_name, "w") as csv_file:
            csvwriter = DictWriter(csv_file, fieldnames=lhs_fieldnames, delimiter=self._delimiter)
            csvwriter.writeheader()

            csvwriter.writerows(new_content)

        return CsvFile(newfile_name, self._delimiter)


class JsonFile(TextFile):
    def _get_ext(self):
        return ".json"

    def _get_specific_content(self, fh: TextIO):
        return json.load(fh)

    def is_list(self):
        content = self.get_file_content()
        return isinstance(content, list)

    def is_object(self):
        content = self.get_file_content()
        return isinstance(content, dict)


class TxtFile(TextFile):
    def _get_ext(self):
        return ".txt"

    def _get_specific_content(self, fh: TextIO):
        return fh.read()

    def get_num_words(self):
        text = self.get_file_content()
        return len(text.split())

    def get_avg_word_len(self):
        words_len = 0
        for word in self.get_file_content().split():
            words_len += len(word)

        return words_len / self.get_num_words()

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise Exception(f"{other} is not a {self._get_ext()} file")

        new_fpath = self._validate_concat_path(other)
        concatenated_content = self.get_file_content() + other.get_file_content()

        with open(new_fpath, "w") as txt_file:
            txt_file.write(concatenated_content)

        return TxtFile(new_fpath)
