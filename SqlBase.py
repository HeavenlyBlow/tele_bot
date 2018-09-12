#_*_ coding: utf-8 _*_

import sqlite3

class SQLigther:

    def __init__(self,databse):
        self.connection = sqlite3.connect(databse)
        self.cursor = self.connection.cursor()

    def select_message(self,client_id):
        with self.connection:
          return self.cursor.execute('SELECT * FROM message WHERE id = ?' (client_id,)).fetchall()[0]

    def count_rows(self):
        with self.connection:
            result = self.cursor.execute('SELECT * FORM message').fetchall()
            return len(result)

    def close(self):
        self.connection.close()


