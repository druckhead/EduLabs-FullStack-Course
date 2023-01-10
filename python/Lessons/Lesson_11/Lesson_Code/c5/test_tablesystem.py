import unittest
from table_system import TableReservationSystem, Table
from tablesystemexceptions import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tables = [Table(1,5), Table(5, 10), Table(6, 9), Table(4, 2)]
        cls.tablesystem = TableReservationSystem(cls.tables, "Japanika")

    def test_reserve(self):
        self.tables[0].reserve(5)
        self.assertFalse(self.tables[0].is_available())
        self.assertTrue(self.tables[0].occupied_seats == 5)

        with self.assertRaises(TableIsAlreadyReservedError):
            self.tables[0].reserve(5)

    def test_release(self):
        self.tables[0].release
        self.assertTrue(self.tables[0].is_available())
        self.assertTrue(self.tables[0].occupied_seats == 0)

        with self.assertRaises(TableIsAlreadyAvailableError):
            self.tables[0].release()

    def test_tablenotfound(self):
        with self.assertRaises(TableNotFoundError):
            self.tablesystem.reserve(6, 6)

        with self.assertRaises(TableNotFoundError):
            self.tablesystem.release(6)



if __name__ == '__main__':
    unittest.main()
