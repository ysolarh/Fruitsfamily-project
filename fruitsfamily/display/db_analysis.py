from data.database.db_module import DatabaseModule


class DBAnalysis:
    def __init__(self):
        self.db_module = DatabaseModule()

    def get_count_by_brand(self, brand: str) -> int:
        sql_count = """SELECT COUNT(*) as count FROM Items WHERE brand_id = 
                    (SELECT brand_id FROM brands WHERE brand_name = %s);"""
        count: dict = self.db_module.executeOne(sql_count, brand)
        print(count['count'], type(count['count'])) # debug
        return count['count']

    def get_count_by_category(self, category: str) -> int:
        sql_count = """SELECT COUNT(*) as count FROM Items WHERE category_id =
                    (SELECT category_id FROM Categories WHERE name = %s);"""
        count: dict = self.db_module.executeOne(sql_count, category)
        return count['count']

    def get_count_brand(self, brand) -> int:
        sql_count = "SELECT COUNT(*) as count FROM Brands;"
        count: dict = self.db_module.executeOne(sql_count, brand)
        return count['count']

    def get_count_category(self) -> int:
        sql_count = "SELECT COUNT(*) as count FROM Categories;"
        count: dict = self.db_module.executeOne(sql_count)
        return count['count']

    def get_categories(self) -> list:
        sql_get = "SELECT name FROM Categories;"
        categories = self.db_module.executeAll(sql_get)
        categories_list = []
        for i in categories:
            categories_list.append(i['name'])
        return categories_list

print(DBAnalysis().get_categories()) # debug