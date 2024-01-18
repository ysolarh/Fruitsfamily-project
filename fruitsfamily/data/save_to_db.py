import pymysql
from config.constants_db import (HOST, USER, PASSWORD, DB, CHARSET, TABLES)


class FruitsDB:
    def __init__(self):
        self.conn = pymysql.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            db=DB,
            charset=CHARSET,
            cursorclass=pymysql.cursors.DictCursor
        )

    def create_tables(self, cur):
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Items (
                item_id INT NOT NULL AUTO INCREMENT,
                category_id INT,
                brand_id INT,
                price INT NOT NULL,
                url TEXT,
                PRIMARY KEY (item_id)
                FOREIGN KEY (category_id) REFERENCES Categories (category_id),
                FOREIGN KEY (brand_id) REFERENCES Brands (brand_id)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Categories (
                category_id INT NOT NULL AUTO INCREMENT,
                name VARCHAR(10) NOT NULL
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Brands (
                brand_id INT NOT NULL AUTO_INCREMENT
                brand_name VARCHAR(50) NOT NULL
            );
        """)

    # def create_db(self):

    def save(self, data_list):
        with self.conn.cursor() as cur:
            self.create_tables(cur)
            # sql = """
            #     INSERT INTO items(
            #     )
            # """
