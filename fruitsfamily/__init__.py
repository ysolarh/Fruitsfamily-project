from data.collecting.crawling import Crawling
from data.database.db_save import FruitsDB
from flask import Flask
import config


from fruitsfamily.data.analysis.graph import ShowGraph

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


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    from .view import main_views
    app.register_blueprint(main_views.bp)

    return app

# if __name__ == "__main__":
#     Application().run()
# app.run()
# app.run(debug=True) # debug
