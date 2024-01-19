import pymysql
from pymysql import IntegrityError
from console.console_writer import ConsoleWriter
from data.database.db_module import DatabaseModule
from config.constants import (URL_IDX, CATE_IDX, BRAND_IDX, PROD_IDX, PRICE_IDX)


class FruitsDB:
    def __init__(self):
        self.db_module = DatabaseModule()

    def create_table_categories(self) -> None:
        sql_create_cate = """
            CREATE TABLE IF NOT EXISTS Categories (
                category_id INT NOT NULL AUTO_INCREMENT,
                name VARCHAR(10) NOT NULL UNIQUE,
                PRIMARY KEY (category_id)
            );
        """
        self.db_module.execute(sql_create_cate)

    def create_table_brands(self) -> None:
        sql_create_brand = """
            CREATE TABLE IF NOT EXISTS Brands (
                brand_id INT NOT NULL AUTO_INCREMENT,
                brand_name VARCHAR(50) NOT NULL UNIQUE,
                Primary KEY (brand_id)
            );
        """
        self.db_module.execute(sql_create_brand)

    def create_table_items(self) -> None:
        sql_create_item = """
            CREATE TABLE IF NOT EXISTS Items (
                item_id INT NOT NULL AUTO_INCREMENT,
                category_id INT,
                brand_id INT,
                product VARCHAR(100) NOT NULL UNIQUE,
                price VARCHAR(10) NOT NULL,
                url TEXT,
                PRIMARY KEY (item_id),
                FOREIGN KEY (category_id) REFERENCES Categories (category_id) ON DELETE CASCADE,
                FOREIGN KEY (brand_id) REFERENCES Brands (brand_id) ON DELETE CASCADE
            );
        """
        self.db_module.execute(sql_create_item)

    def create_tables(self) -> None:
        self.create_table_categories()
        self.create_table_brands()
        self.create_table_items()

    def insert_categories(self, data: tuple) -> None:
        sql_cate = "INSERT INTO Categories (name) VALUES (%s);"
        try:
            self.db_module.execute(sql_cate, data[CATE_IDX])
        except IntegrityError as e:
            ConsoleWriter.print_error(e)

    def insert_brands(self, data: tuple) -> None:
        sql_brand = "INSERT INTO Brands (brand_name) VALUES (%s);"
        try:
            self.db_module.execute(sql_brand, data[BRAND_IDX])
        except IntegrityError as e:
            ConsoleWriter.print_error(e)

    def insert_items(self, data: tuple) -> None:
        sql_item = """
                INSERT INTO Items (category_id, brand_id, product, price, url) VALUES (
                    (SELECT category_id FROM Categories WHERE name = %s),
                    (SELECT brand_id FROM Brands WHERE brand_name = %s),
                    %s, %s, %s
                );"""
        try:
            self.db_module.execute(sql_item, (data[CATE_IDX], data[BRAND_IDX], data[PROD_IDX], data[PRICE_IDX][:-1], data[URL_IDX]))
        except IntegrityError as e:
            ConsoleWriter.print_error(e)

    def insert_datas(self, data_list: list) -> None:
        for data in data_list:
            self.insert_categories(data)
            self.insert_brands(data)
            self.db_module.commit()
            self.insert_items(data)
            self.db_module.commit()

    def save_db(self, data_list: list) -> None:
        try:
            self.create_tables()
            self.insert_datas(data_list)
        except Exception as e: # fix
            ConsoleWriter.print_error(e)
        finally:
            self.db_module.close_db()
