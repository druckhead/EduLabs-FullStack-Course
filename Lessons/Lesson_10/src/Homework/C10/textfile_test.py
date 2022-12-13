import os.path
import unittest
from textfile import TxtFile, CsvFile, JsonFile, TextFile
from customexceptions import *
from os import system
import os.path


class TextFileTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if os.path.exists("/Users/danielraz/EduLabs-FullStack-Course/Lessons/"
                          "Lesson_10/src/Homework/C10/files/testCsv_testCsv2.csv"):
            system("rm -rf /Users/danielraz/EduLabs-FullStack-Course/Lessons/"
                   "Lesson_10/src/Homework/C10/files/testCsv_testCsv2.csv")
            print(f"deleted /Users/danielraz/EduLabs-FullStack-Course/Lessons/"
                  "Lesson_10/src/Homework/C10/files/testCsv_testCsv2.csv")
        if os.path.exists(
                "/Users/danielraz/EduLabs-FullStack-Course/Lessons/Lesson_10/src/Homework/C10/files/text_text2.txt"):
            system("rm -rf /Users/danielraz/EduLabs-FullStack-Course/Lessons/"
                   "Lesson_10/src/Homework/C10/files/text_text2.txt")
            print(
                "deleted /Users/danielraz/EduLabs-FullStack-Course/"
                "Lessons/Lesson_10/src/Homework/C10/files/text_text2.txt")

        cls.txt1 = TxtFile(
            "/Users/danielraz/EduLabs-FullStack-Course/Lessons/Lesson_10/src/Homework/C10/files/text.txt")
        cls.txt2 = TxtFile(
            "/Users/danielraz/EduLabs-FullStack-Course/Lessons/Lesson_10/src/Homework/C10/files/text2.txt")
        cls.json1 = JsonFile(
            "files/testJsonFile.json")
        cls.json2 = JsonFile(
            "files/testJsonFile2.json")
        cls.csv1 = CsvFile(
            "files/testCsv.csv")
        cls.csv2 = CsvFile(
            "/Users/danielraz/EduLabs-FullStack-Course/Lessons/Lesson_10/src/Homework/C10/files/testCsv2.csv")
        cls.csv3 = CsvFile(
            "/Users/danielraz/EduLabs-FullStack-Course/Lessons/Lesson_10/src/Homework/C10/files/testCsv3.csv")

        cls.files = [cls.txt1, cls.txt2, cls.json1, cls.json2, cls.csv1, cls.csv2, cls.csv3]

        cls.txt1_text = "Hello, world\n\n" \
                        "My name is daniel this a test of txt file functions\n\n" \
                        "this is a program in the Python programming language\n"
        cls.txt2_text = "This is the second txt file\n\n" \
                        "this is so cool\n"
        cls.txt1_txt2_text = "Hello, world\n\n" \
                             "My name is daniel this a test of txt file functions\n\n" \
                             "this is a program in the Python programming language\n" \
                             "This is the second txt file\n\n" \
                             "this is so cool\n"

        cls.json_content = {
            "name": "Daniel Raz",
            "age": 26,
            "occupation": "Developer",
            "family": {
                "brother": True,
                "sister": True,
                "father": True,
                "mother": True
            }
        }
        cls.json2_content = [
            {
                "name": "daniel",
                "age": 26,
                "location": "Here"
            },
            {
                "name": "daniel",
                "age": 26,
                "location": "Here"
            }
        ]

        cls.csv1_content = [
            {'Year': '1980', 'avg salary': '0.1234', 'days': '0.111', 'month': '0.15611', 'weeks': '0.210',
             'age': '0.0'},
            {'Year': '1981', 'avg salary': '0.1235', 'days': '0.211', 'month': '0.15612', 'weeks': '0.29',
             'age': '0.1'},
            {'Year': '1982', 'avg salary': '0.1236', 'days': '0.311', 'month': '0.15613', 'weeks': '0.28',
             'age': '0.2'},
            {'Year': '1983', 'avg salary': '0.1237', 'days': '0.411', 'month': '0.15614', 'weeks': '0.27',
             'age': '0.3'},
            {'Year': '1984', 'avg salary': '0.1238', 'days': '0.511', 'month': '0.15615', 'weeks': '0.26',
             'age': '0.4'},
            {'Year': '1985', 'avg salary': '0.1239', 'days': '0.611', 'month': '0.15616', 'weeks': '0.24',
             'age': '0.5'},
            {'Year': '1986', 'avg salary': '0.12310', 'days': '0.7111', 'month': '0.15617', 'weeks': '0.23',
             'age': '0.6'},
            {'Year': '1987', 'avg salary': '0.12311', 'days': '0.811', 'month': '0.15618', 'weeks': '0.22',
             'age': '0.7'},
            {'Year': '1988', 'avg salary': '0.12312', 'days': '0.911', 'month': '0.15619', 'weeks': '0.21',
             'age': '0.8'}]
        cls.csv2_content = [
            {'Year': '1989', 'days': '0.1239', 'avg salary': '0.611', 'month': '0.15616', 'weeks': '0.24',
             'age': '0.01'},
            {'Year': '1990', 'days': '0.12310', 'avg salary': '0.7111', 'month': '0.15617', 'weeks': '0.23',
             'age': '0.02'},
            {'Year': '1991', 'days': '0.12311', 'avg salary': '0.811', 'month': '0.15618', 'weeks': '0.22',
             'age': '0.03'},
            {'Year': '1992', 'days': '0.12312', 'avg salary': '0.911', 'month': '0.15619', 'weeks': '0.21',
             'age': '0.04'},
            {'Year': '1993', 'days': '0.1238', 'avg salary': '0.511', 'month': '0.15615', 'weeks': '0.26',
             'age': '0.05'}]
        cls.csv1_csv2_content = [
            {'Year': '1980', 'avg salary': '0.1234', 'days': '0.111', 'month': '0.15611', 'weeks': '0.210',
             'age': '0.0'},
            {'Year': '1981', 'avg salary': '0.1235', 'days': '0.211', 'month': '0.15612', 'weeks': '0.29',
             'age': '0.1'},
            {'Year': '1982', 'avg salary': '0.1236', 'days': '0.311', 'month': '0.15613', 'weeks': '0.28',
             'age': '0.2'},
            {'Year': '1983', 'avg salary': '0.1237', 'days': '0.411', 'month': '0.15614', 'weeks': '0.27',
             'age': '0.3'},
            {'Year': '1984', 'avg salary': '0.1238', 'days': '0.511', 'month': '0.15615', 'weeks': '0.26',
             'age': '0.4'},
            {'Year': '1985', 'avg salary': '0.1239', 'days': '0.611', 'month': '0.15616', 'weeks': '0.24',
             'age': '0.5'},
            {'Year': '1986', 'avg salary': '0.12310', 'days': '0.7111', 'month': '0.15617', 'weeks': '0.23',
             'age': '0.6'},
            {'Year': '1987', 'avg salary': '0.12311', 'days': '0.811', 'month': '0.15618', 'weeks': '0.22',
             'age': '0.7'},
            {'Year': '1988', 'avg salary': '0.12312', 'days': '0.911', 'month': '0.15619', 'weeks': '0.21',
             'age': '0.8'},
            {'Year': '1989', 'avg salary': '0.611', 'days': '0.1239', 'month': '0.15616', 'weeks': '0.24',
             'age': '0.01'},
            {'Year': '1990', 'avg salary': '0.7111', 'days': '0.12310', 'month': '0.15617', 'weeks': '0.23',
             'age': '0.02'},
            {'Year': '1991', 'avg salary': '0.811', 'days': '0.12311', 'month': '0.15618', 'weeks': '0.22',
             'age': '0.03'},
            {'Year': '1992', 'avg salary': '0.911', 'days': '0.12312', 'month': '0.15619', 'weeks': '0.21',
             'age': '0.04'},
            {'Year': '1993', 'avg salary': '0.511', 'days': '0.1238', 'month': '0.15615', 'weeks': '0.26',
             'age': '0.05'}]

    @classmethod
    def tearDownClass(cls) -> None:
        system("rm -rf /Users/danielraz/EduLabs-FullStack-Course/Lessons/"
               "Lesson_10/src/Homework/C10/files/testCsv_testCsv2.csv")
        system("rm -rf /Users/danielraz/EduLabs-FullStack-Course/Lessons/"
               "Lesson_10/src/Homework/C10/files/text_text2.txt")
        print("deleted files that were created during tests")

    def test_invalid_path(self):
        path = "/Users/danielrazz/EduLabs-FullStack-Course/Lessons/Lesson_10/src/Homework/C10/files/text.txt"
        with self.assertRaises(FileNotFoundError):
            _ = TxtFile(path)

    def test_invalid_ext(self):
        path = "/Users/danielraz/EduLabs-FullStack-Course/Lessons/Lesson_10/src/Homework/C10/files/test.txtt"
        with self.assertRaises(InvalidFileExtension):
            _ = TxtFile(path)

    def test_open_files(self):
        for file in self.files:
            self.assertIsInstance(file, TextFile)

        self.assertIsInstance(self.txt1, TxtFile)
        self.assertIsInstance(self.txt2, TxtFile)
        self.assertIsInstance(self.json1, JsonFile)
        self.assertIsInstance(self.json2, JsonFile)
        self.assertIsInstance(self.csv1, CsvFile)
        self.assertIsInstance(self.csv2, CsvFile)

    def test_num_rows(self):
        self.assertEqual(self.csv1.get_num_rows(), 9)
        self.assertEqual(self.csv2.get_num_rows(), 5)

    def test_num_cols(self):
        self.assertEqual(self.csv1.get_num_cols(), 6)
        self.assertEqual(self.csv2.get_num_cols(), 6)

    def test_get_content(self):
        self.assertEqual(self.txt1_text, self.txt1.get_file_content())
        self.assertEqual(self.txt2_text, self.txt2.get_file_content())
        self.assertEqual(self.json_content, self.json1.get_file_content())
        self.assertEqual(self.csv1_content, self.csv1.get_file_content())
        self.assertEqual(self.csv2_content, self.csv2.get_file_content())

    def test_get_file_size(self):
        self.assertEqual(357, self.csv1.get_file_size())
        self.assertEqual(220, self.csv2.get_file_size())
        self.assertEqual(167, self.json1.get_file_size())
        self.assertEqual(120, self.txt1.get_file_size())
        self.assertEqual(45, self.txt2.get_file_size())

    def test_get_row(self):
        expected = {'Year': '1983', 'avg salary': '0.1237', 'days': '0.411', 'month': '0.15614', 'weeks': '0.27',
                    'age': '0.3'}
        self.assertEqual(expected, self.csv1.get_row(4))
        expected = {'Year': '1988', 'avg salary': '0.12312', 'days': '0.911', 'month': '0.15619', 'weeks': '0.21',
                    'age': '0.8'}
        self.assertEqual(expected, self.csv1.get_row(9))

        with self.assertRaises(IndexError):
            self.csv1.get_row(0)
        with self.assertRaises(IndexError):
            self.csv1.get_row(20)

    def test_get_col(self):
        expected = ['0.1234', '0.1235', '0.1236', '0.1237', '0.1238', '0.1239', '0.12310', '0.12311', '0.12312']
        self.assertEqual(expected, self.csv1.get_col(2))

        with self.assertRaises(IndexError):
            self.csv1.get_col(0)
        with self.assertRaises(IndexError):
            self.csv1.get_col(50)

    def test_get_cell(self):
        expected = "1980"
        self.assertEqual(expected, self.csv1.get_cell(1, 1))

        with self.assertRaises(IndexError):
            self.csv1.get_cell(0, 1)
        with self.assertRaises(IndexError):
            self.csv1.get_cell(1, 0)
        with self.assertRaises(IndexError):
            self.csv1.get_cell(0, 20)
        with self.assertRaises(IndexError):
            self.csv1.get_cell(20, 0)

    def test_is_list(self):
        self.assertFalse(self.json1.is_list())
        self.assertTrue(self.json2.is_list())

    def test_is_object(self):
        self.assertTrue(self.json1.is_object())
        self.assertFalse(self.json2.is_object())

    def test_add(self):
        new_file = self.txt1 + self.txt2
        self.assertIsInstance(new_file, TextFile)
        self.assertIsInstance(new_file, TxtFile)
        self.assertEqual(self.txt1_txt2_text, new_file.get_file_content())
        with self.assertRaises(FileExistsError):
            self.txt1 + self.txt2

        new_file2 = self.csv1 + self.csv2
        self.assertIsInstance(new_file2, TextFile)
        self.assertIsInstance(new_file2, CsvFile)
        self.assertEqual(self.csv1_csv2_content, new_file2.get_file_content())
        with self.assertRaises(FileExistsError):
            self.csv1 + self.csv2

        with self.assertRaises(IncompatibleFileTypeError):
            self.txt1 + self.json1
        with self.assertRaises(IncompatibleFileTypeError):
            self.txt1 + self.csv1
        with self.assertRaises(IncompatibleFileTypeError):
            self.csv2 + self.json1
        with self.assertRaises(IncompatibleFileTypeError):
            self.txt1 + "some random text"

        with self.assertRaises(IncompatibleCsvHeaders):
            self.csv1 + self.csv3
        with self.assertRaises(IncompatibleCsvHeaders):
            self.csv2 + self.csv3


if __name__ == '__main__':
    unittest.main()
