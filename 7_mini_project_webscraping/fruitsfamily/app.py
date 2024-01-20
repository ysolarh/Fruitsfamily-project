from fruitsfamily.data.collecting.crawling import Crawling
from fruitsfamily.data.database.db_save import FruitsDB


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


if __name__ == "__main__":
    Application().run()
