import pymysql
from pymysql import IntegrityError
from console.console_writer import ConsoleWriter

from config.constants_db import (HOST, USER, PASSWORD, DB, CHARSET, TABLES)
from config.constants import (URL_IDX, CATE_IDX, BRAND_IDX, PROD_IDX, PRICE_IDX)


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
            CREATE TABLE IF NOT EXISTS Categories (
                category_id INT NOT NULL AUTO_INCREMENT,
                name VARCHAR(10) NOT NULL UNIQUE,
                PRIMARY KEY (category_id)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Brands (
                brand_id INT NOT NULL AUTO_INCREMENT,
                brand_name VARCHAR(50) NOT NULL UNIQUE,
                Primary KEY (brand_id)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Items (
                item_id INT NOT NULL AUTO_INCREMENT,
                category_id INT,
                brand_id INT,
                product VARCHAR(100) NOT NULL,
                price VARCHAR(10) NOT NULL,
                url TEXT,
                PRIMARY KEY (item_id),
                FOREIGN KEY (category_id) REFERENCES Categories (category_id) ON DELETE CASCADE,
                FOREIGN KEY (brand_id) REFERENCES Brands (brand_id) ON DELETE CASCADE
            );
        """)

    def insert_datas(self, cur, data_list):
        for i in data_list:
            sql_for_cate = "INSERT INTO Categories (name) VALUES (%s)"
            sql_for_brand = "INSERT INTO Brands (brand_name) VALUES (%s)"
            try:
                cur.execute(sql_for_cate, i[CATE_IDX])
            except IntegrityError as e:
                ConsoleWriter.print_error(e)
            try:
                cur.execute(sql_for_brand, i[BRAND_IDX])
            except IntegrityError as e:
                ConsoleWriter.print_error(e)

            self.conn.commit()
            # price = int(i[PRICE_IDX][:-1].replace(",", ""))
            sql_for_item = """
                INSERT INTO Items (category_id, brand_id, product, price, url) VALUES (
                    (SELECT category_id FROM Categories WHERE name = %s),
                    (SELECT brand_id FROM Brands WHERE brand_name = %s),
                    %s, %s, %s)
            """
            cur.execute(sql_for_item, (i[CATE_IDX], i[BRAND_IDX], i[PROD_IDX], i[PRICE_IDX][:-1], i[URL_IDX]))
            self.conn.commit()

    def save(self, data_list):
        with self.conn.cursor() as cur:
            self.create_tables(cur)
            self.insert_datas(cur, data_list)
