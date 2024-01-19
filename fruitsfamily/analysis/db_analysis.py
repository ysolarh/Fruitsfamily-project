import sys
from data.database.db_module import DatabaseModule


class DBAnalysis:
    def __init__(self):
        self.db_module = DatabaseModule()

    def get_count_by_brand(self, brand: str) -> int:
        sql_count = """SELECT COUNT(*) as count FROM Items WHERE brand_id = 
                    (SELECT brand_id FROM brands WHERE brand_name = %s);"""
        count: dict = self.db_module.execute_one(sql_count, brand)
        # print(count, count['count'], type(count['count']), type(count))  # debug
        return count['count']

    def get_count_by_category(self, category: str) -> int:
        sql_count = """SELECT COUNT(*) as count FROM Items WHERE category_id =
                    (SELECT category_id FROM Categories WHERE name = %s);"""
        count: dict = self.db_module.execute_one(sql_count, category)
        return count['count']

    def get_count_brand(self, brand) -> int:
        sql_count = "SELECT COUNT(*) as count FROM Brands;"
        count: dict = self.db_module.execute_one(sql_count, brand)
        return count['count']

    def get_count_category(self) -> int:
        sql_count = "SELECT COUNT(*) as count FROM Categories;"
        count: dict = self.db_module.execute_one(sql_count)
        return count['count']

    def get_categories(self) -> list:
        sql_get = "SELECT name FROM Categories;"
        categories = self.db_module.execute_all(sql_get)
        categories_list = []
        for i in categories:
            categories_list.append(i['name'])
        return categories_list

    def get_count_by_price(self, start: int, end: int) -> int:
        sql_count = "SELECT COUNT(*) as count FROM Items WHERE price >= %s AND price < %s;"
        count: dict = self.db_module.execute_one(sql_count, (start, end))
        return count['count']

    def get_counts_by_price_range(self) -> list:
        price_range = [n * 100000 for n in range(10)] + [n * 1000000 for n in range(1, 11)]
        count_list = []
        for i in range(len(price_range) - 1):
            count_list.append(self.get_count_by_price(price_range[i], price_range[i + 1]))
        count_list.append(self.get_count_by_price(price_range[-1], sys.maxsize))
        return count_list


# print(DBAnalysis().get_categories()) # debug
# print(DBAnalysis().get_count_by_brand("dior"))
# print(DBAnalysis().get_counts_by_price_range())