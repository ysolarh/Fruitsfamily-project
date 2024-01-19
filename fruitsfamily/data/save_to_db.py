import pymysql
from pymysql import IntegrityError
from console.console_writer import ConsoleWriter
from config.constants_db import (HOST, USER, PASSWORD, DB, CHARSET)
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

    def create_table_cates(self, cur):
        sql_create_cate = """
            CREATE TABLE IF NOT EXISTS Categories (
                category_id INT NOT NULL AUTO_INCREMENT,
                name VARCHAR(10) NOT NULL UNIQUE,
                PRIMARY KEY (category_id)
            );
        """
        cur.execute(sql_create_cate)

    def create_table_brands(self, cur):
        sql_create_brand = """
            CREATE TABLE IF NOT EXISTS Brands (
                brand_id INT NOT NULL AUTO_INCREMENT,
                brand_name VARCHAR(50) NOT NULL UNIQUE,
                Primary KEY (brand_id)
            );
        """
        cur.execute(sql_create_brand)

    def create_table_items(self, cur):
        sql_create_item = """
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
        """
        cur.execute(sql_create_item)

    def create_tables(self, cur):
        self.create_table_cates(cur)
        self.create_table_brands(cur)
        self.create_table_items(cur)

    def insert_cates(self, cur, data):
        sql_cate = "INSERT INTO Categories (name) VALUES (%s)"
        try:
            cur.execute(sql_cate, data[CATE_IDX])
        except IntegrityError as e:
            ConsoleWriter.print_error(e)

    def insert_brands(self, cur, data):
        sql_brand = "INSERT INTO Brands (brand_name) VALUES (%s)"
        try:
            cur.execute(sql_brand, data[BRAND_IDX])
        except IntegrityError as e:
            ConsoleWriter.print_error(e)

    def insert_items(self, cur, data):
        sql_item = """
                INSERT INTO Items (category_id, brand_id, product, price, url) VALUES (
                    (SELECT category_id FROM Categories WHERE name = %s),
                    (SELECT brand_id FROM Brands WHERE brand_name = %s),
                    %s, %s, %s
                )"""
        cur.execute(sql_item, (data[CATE_IDX], data[BRAND_IDX], data[PROD_IDX], data[PRICE_IDX][:-1], data[URL_IDX]))

    def insert_datas(self, cur, data_list):
        for data in data_list:
            self.insert_cates(cur, data)
            self.insert_brands(cur, data)
            self.conn.commit()
            self.insert_items(cur, data)
            self.conn.commit()

    def save(self, data_list):
        with self.conn.cursor() as cur:
            self.create_tables(cur)
            self.insert_datas(cur, data_list)
