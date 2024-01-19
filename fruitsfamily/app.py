from data.crawling import Crawling
from console.console_writer import ConsoleWriter
from data.save_to_db import FruitsDB


class Application:
    def __init__(self):
        self.__running = True
        self.datas = []

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

            FruitsDB().save(self.datas)


if __name__ == "__main__":
    Application().run()
