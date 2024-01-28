SQL_BASE = "SELECT I.item_id AS id, C.name AS category, B.brand_name AS brand, I.product AS product, I.price AS price, I.url AS url, I.date AS date, I.sold AS sold \
    FROM Items I \
    JOIN Categories C ON I.category_id = C.category_id \
    JOIN Brands B ON I.brand_id = B.brand_id "
ORDER_DESC = "ORDER BY date DESC"
ORDER_ASC = "ORDER BY date ASC"

SQL_CATE = "SELECT category_id, name FROM Categories;"

SQL_SEARCH_PRODUCT = SQL_BASE + "WHERE INSTR(product, %s)" + ORDER_DESC
SQL_SEARCH_BRAND = SQL_BASE + "WHERE INSTR(brand, %s)" + ORDER_DESC
SQL_SEARCH_CATE = SQL_BASE + "WHERE INSTR(category, %s)" + ORDER_DESC
SQL_ALL = SQL_BASE + ORDER_DESC
