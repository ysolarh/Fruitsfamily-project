from data.collecting.crawling import Crawling
from data.database.db_save import FruitsDB


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


if __name__ == "__main__":
    Application().run()
