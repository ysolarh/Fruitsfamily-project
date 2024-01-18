from data.crawling import Crawling
from console.console_writer import ConsoleWriter
# from utils.file_utils import FileUtils

class Application:
    def __init__(self):
        self.__running = True
        # FileUtils.set_path()

    def run(self):
        if self.__running:
            crawling = Crawling()
            crawling.crawl()
            # try:
            #     # crawling.crawl()
            #     # db()
            #     # display()
            # except:
            #     ConsoleWriter.print_error()
            # finally:
            #     crawling.stop()


if __name__ == "__main__":
    Application().run()
