import pymysql
from config.constants_db import (HOST, USER, PASSWORD, DB, CHARSET)

class DatabaseModule:
    def __init__(self):
        self.conn = pymysql.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            db=DB,
            charset=CHARSET,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    def close_db(self) -> None:
        self.conn.close()

    def commit(self) -> None:
        self.conn.commit()

    def execute(self, query: str, *args: tuple) -> None:
        # self.cur.execute(query, args or ()) # fix
        self.cur.execute(query, *args)

    def executeOne(self, query, *args: tuple) -> tuple:
        self.cur.execute(query, *args)
        row = self.cur.fetchone()
        return row

    def executeAll(self, query, *args: tuple) -> tuple:
        self.cur.execute(query, *args)
        rows = self.cur.fetchall()
        return rows
