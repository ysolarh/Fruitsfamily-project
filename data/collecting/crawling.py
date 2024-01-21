from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from console.console_writer import ConsoleWriter
from config.constants import (FRUITS_URL, SLEEP_TIME, SCROLL_PAUSE_TIME, SCROLL_TIMES)


class Crawling:
    def __init__(self):
        self.url = FRUITS_URL
        self.user_agent = {"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/120.0.0.0 Safari/537.36"}
        self.options = Options()
        self.set_options()
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.get(self.url)

    def set_options(self) -> None:
        self.options.add_argument(f"user-agent={self.user_agent}")
        self.options.add_argument('incognito')
        # self.options.add_argument('--headless')

    def get_scroll_height(self) -> int:
        return self.driver.execute_script("return document.body.scrollHeight")

    def scroll_one(self) -> None:
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_all(self) -> None:
        last_height = self.get_scroll_height()
        while True:
            self.scroll_one()
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = self.get_scroll_height()
            if new_height == last_height:
                break
            last_height = new_height

    def scroll_n_times(self, n: int) -> None:
        i = 0
        while i < n:
            self.scroll_one()
            time.sleep(SCROLL_PAUSE_TIME)
            i += 1

    def extract_item_links(self) -> list:
        datas = self.driver.find_elements(By.CLASS_NAME, "CardDeck-item")
        item_links = []
        for i in datas:
            item = i.find_element(By.CLASS_NAME, "ProductPreview")
            link = item.get_attribute("href")
            item_links.append(link)
        return item_links

    def extract_item_infos(self, item_links: list) -> list:
        items_info = []
        # for link in item_links[:5]:  # debug
        for link in item_links:
            self.driver.get(link)
            category = self.extract_item_category()
            brand = self.extract_item_brand()
            product = self.extract_item_product()
            price = self.extract_item_price()
            is_sold = self.extract_is_sold()
            items_info.append((link, category, brand, product, price, is_sold))
            time.sleep(SLEEP_TIME)
        return items_info

    def extract_item_category(self) -> str:
        category = self.driver.find_elements(By.CLASS_NAME, "Product-tag")[0].text
        return category

    def extract_item_brand(self) -> str:
        brand = self.driver.find_elements(By.CLASS_NAME, "Product-tag")[1].text
        return brand

    def extract_item_product(self) -> str:
        product = self.driver.find_element(By.CLASS_NAME, "Product-title").text
        return product

    def extract_item_price(self) -> str:
        price = self.driver.find_element(By.CLASS_NAME, "Product-price").text
        return price

    def extract_is_sold(self) -> int:
        is_sold = self.driver.find_element(By.CLASS_NAME, "Product-buy").text
        if is_sold == '품절':
            return 1
        else:
            return 0

    def crawl(self) -> list:
        try:
            self.scroll_n_times(SCROLL_TIMES) # debug
            item_links = self.extract_item_links()
            item_infos = self.extract_item_infos(item_links)
            print(item_infos) # debug
            return item_infos
        except Exception as e: # fix
            ConsoleWriter.print_error(e)
        finally:
            self.close_driver()

    def close_driver(self) -> None:
        self.driver.close()
