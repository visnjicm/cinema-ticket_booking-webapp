import sqlite3


class SQLTable:
    conn = ""
    cursor = ""
    sql_expression = ""
    sql_parameters = ()
    row = ()
    column_names = []
    database = ""
    table_name = ""

    def __init__(self, database, table):
        self.database = database
        self.table_name = table
        self.open_sql_connection()

    def _get_column_names(self):
        self.sql_expression = f"PRAGMA table_info({self.table_name})"
        self.cursor.execute(self.sql_expression)
        columns = self.cursor.fetchall()
        self.column_names = [column[1] for column in columns]

    def close_and_reopen_sql_connection(self):
        self.close_sql_connection()
        self.open_sql_connection()

    def open_sql_connection(self):
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
        self._get_column_names()

    # def select_row(self):
    #     self.sql_expression = f'SELECT * FROM {self.table_name} WHERE seat_id = ?'
    #     self.sql_parameters = (self.seat_id,)
    #     self.cursor.execute(self.sql_expression, self.sql_parameters)
    #     self.row = self.cursor.fetchone()

    def close_sql_connection(self):
        self.cursor.close()
        self.conn.close()
