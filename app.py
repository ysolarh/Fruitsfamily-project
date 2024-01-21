from data.collecting.crawling import Crawling
from data.database.db_module import DatabaseModule
from data.database.db_save import FruitsDB
from flask import Flask, render_template


# from analysis.graph import ShowGraph

class Application:
    def __init__(self):
        self.__running = True
        self.datas = []

    def run(self):
        if self.__running:
            crawling = Crawling()
            fruits_db = FruitsDB()
            self.datas = crawling.crawl()
            fruits_db.save_db(self.datas)
            # ShowGraph().show_by_category() # debug


app = Flask(__name__)
db_module = DatabaseModule()
cur = db_module.cur
sql = ("SELECT C.name AS category, B.brand_name AS brand, I.product AS product, I.price AS price, I.url AS url \
    FROM Items I \
    JOIN Categories C ON I.category_id = C.category_id \
    JOIN Brands B ON I.brand_id = B.brand_id")
fruits_data = db_module.execute_all(sql)


# fruits_data = db_module.fetch_all()

@app.route('/')
def index():
    return render_template('index.html', data_list=fruits_data)


if __name__ == "__main__":
    Application().run()
    app.run(debug=True)
