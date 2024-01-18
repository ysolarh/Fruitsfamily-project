from data.crawling import Crawling
from console.console_writer import ConsoleWriter
from data.save_to_db import FruitsDB
# from utils.file_utils import FileUtils

class Application:
    def __init__(self):
        self.__running = True
        self.datas = []
        # FileUtils.set_path()

    def run(self):
        if self.__running:
            crawling = Crawling()
            try:
                self.datas = crawling.crawl()
                # display()
            except:
                ConsoleWriter.print_error()
            finally:
                crawling.stop()

            # try:
            FruitsDB().save(self.datas)
            # except raise_mysql_exception:
            #     ConsoleWriter.print_error()


if __name__ == "__main__":
    Application().run()
