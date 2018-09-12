# _*_ coding: utf-8 _*_

import sqlite3

class mySQL:
    def __init__(self,database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def registration(self,number,name,points):
        with self.connection:
            self.cursor.execute("INSERT INTO Message VALUES (?,?,?)", (number,name,points,))
            return True

    def closse(self):
        self.connection.close()

    # def creature_sql_inquiry(self,chat_id,message):
