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

    def close_db(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def execute(self, query, *args):
        self.cur.execute(query, *args)
