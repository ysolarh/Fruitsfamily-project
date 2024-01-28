from flask import Flask

from fruitsfamily.data.analysis.graph2 import ShowGraph
from fruitsfamily.data.collecting.crawling import Crawling
from fruitsfamily.data.database.db_save import FruitsDB
from fruitsfamily.configs import config


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


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    from .view import main_views
    app.register_blueprint(main_views.bp)

    return app


# if __name__ == "__main__":
#     Application().run() # update할때 작동시킬것
# app.run()
# app.run(debug=True) # debug

ShowGraph().show_bar_graph()  # debug
