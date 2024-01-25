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


from data.database.db_query import SQL_ALL, SQL_CATE

app = Flask(__name__)
db_module = DatabaseModule()
cur = db_module.cur
fruits_data = db_module.execute_all(SQL_ALL)
category_data = db_module.execute_all(SQL_CATE)


@app.route('/')
def index():
    return render_template('index.html', data_list=fruits_data, cate_list=category_data)


if __name__ == "__main__":
    Application().run()
    app.run()
    # app.run(debug=True) # debug
