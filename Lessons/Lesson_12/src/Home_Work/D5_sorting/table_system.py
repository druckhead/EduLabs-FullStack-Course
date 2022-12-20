import datetime
import os.path
import pickle


class Table:

    def __init__(self, table_id, seats, max_time_limit=datetime.timedelta(minutes=90)):
        self.table_id = table_id
        self.seats = seats
        self.occupied_seats = 0
        self.start_time = None
        self.location = None
        self.max_time_limit = max_time_limit

    def is_available(self):
        return self.occupied_seats == 0

    def reserve(self, guests_num) -> bool:

        # we allow to reserve a table only if it's available
        # and amount fo guests fits the amount of seats
        if self.occupied_seats == 0 and self.seats >= guests_num:
            self.occupied_seats = guests_num
            self.start_time = datetime.datetime.utcnow()
            return True
        return False

    def release(self) -> bool:

        # The table is already available
        if self.occupied_seats == 0:
            return False

        self.occupied_seats = 0
        self.start_time = None

    def _get_end_time(self):
        return self.start_time + self.max_time_limit

    def time_left(self) -> datetime.timedelta:

        if not self.start_time:
            return datetime.timedelta()
        return self._get_end_time() - datetime.datetime.utcnow()

    def get_available_time(self) -> datetime.datetime:

        if not self.start_time:
            return datetime.datetime.utcnow()

        return self.start_time + self.max_time_limit

    def __str__(self):
        return f"Table id {self.table_id}, seats: {self.seats}, available: {self.is_available()}"

    def __repr__(self):
        return f"Table {self.table_id} ({self.seats} timeleft: {self.time_left()})"


class TableReservationSystem:

    def __init__(self, tables_list: list, name: str,
                 max_time_limit: datetime.timedelta = datetime.timedelta(minutes=90)):

        self.name = name
        self.max_time_limit = max_time_limit

        self.tables: list[Table] = []
        for i, table_seats in enumerate(tables_list):
            self.tables.append(Table(table_id=i, seats=table_seats, max_time_limit=self.max_time_limit))

    def reserve(self, guests_num, table_id) -> bool:
        for table in self.tables:
            if table.table_id == table_id:
                return table.reserve(guests_num)

        # table with provided id does not exist
        return False

    def release(self, table_id) -> bool:
        for table in self.tables:
            if table.table_id == table_id:
                return table.release()
        return False

    def get_available_tables(self, guests_num) -> list[Table]:
        """

        :param guests_num:
        :return: list of relevant tables sorted by seats ascending
        Note the return value must be list to preserve order!
        """

        available_tables = []

        for table in self.tables:
            if table.seats >= guests_num and table.is_available():
                available_tables.append(table)

        sorted_tables = sorted(available_tables, key=lambda curr_table: curr_table.seats)

        return sorted_tables

    def get_soonest_available_tables(self, guests_num) -> list[Table]:

        # get suitable tables
        suitable_tables: list[Table] = []

        for table in self.tables:
            if table.seats >= guests_num:
                suitable_tables.append(table)

        sorted_tables = sorted(
            sorted(suitable_tables, key=lambda curr_table: curr_table.get_available_time(), reverse=True),
            key=lambda curr_table: (curr_table.get_available_time(), curr_table.seats)
        )

        return sorted_tables
