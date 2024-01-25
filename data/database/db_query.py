SQL_ALL = ("SELECT I.item_id AS id, C.name AS category, B.brand_name AS brand, I.product AS product, I.price AS price, I.url AS url, I.date AS date, I.sold AS sold \
    FROM Items I \
    JOIN Categories C ON I.category_id = C.category_id \
    JOIN Brands B ON I.brand_id = B.brand_id \
    ORDER BY date DESC;")
SQL_CATE = "SELECT category_id, name FROM Categories;"
# SEARCH_QUERY = "SELECT  FROM "
