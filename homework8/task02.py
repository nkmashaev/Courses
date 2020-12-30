import os
import sqlite3
from typing import Any, Callable


class TableData:
    def __init__(self, database_name: str, table_name: str):
        self.database_name = os.path.join(os.path.dirname(__file__), database_name)
        self.table_name = table_name

    def __get_cursor(self):
        conn = sqlite3.connect(self.database_name)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        return cursor

    def __len__(self):
        cursor = self.__get_cursor()
        cursor.execute(f"SELECT COUNT(*) from {self.table_name}")
        return cursor.fetchone()[0]

    def __getitem__(self, item):
        cursor = self.__get_cursor()
        cursor.execute(f"SELECT * from {self.table_name} where name=?", (item,))
        return tuple(cursor.fetchone())

    def __contains__(self, item):
        cursor = self.__get_cursor()
        cursor.execute(f"SELECT * from {self.table_name} where name=?", (item,))
        return False if cursor.fetchone() is None else True

    def __iter__(self):
        cursor = self.__get_cursor()
        cursor.execute(f"SELECT * from {self.table_name}")
        while True:
            curr_row = cursor.fetchone()
            if curr_row is None:
                break
            yield curr_row
