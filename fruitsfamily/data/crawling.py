from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from config.constants import (FRUITS_URL, SLEEP_TIME, SCROLL_PAUSE_TIME)


class Crawling:
    def __init__(self):
        self.url = FRUITS_URL
        self.user_agent = {"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/120.0.0.0 Safari/537.36"}
        self.options = Options()
        self.set_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self.url)

    def set_options(self):
        self.options.add_argument(f"user-agent={self.user_agent}")
        self.options.add_argument('incognito')
        # self.options.add_argument('--headless')

    def scroll(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

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
        for link in item_links[:5]:  #
            self.driver.get(link)
            category = self.extract_item_category()
            brand = self.extract_item_brand()
            product = self.extract_item_product()
            price = self.extract_item_price()
            items_info.append((link, category, brand, product, price))
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

    def crawl(self) -> list:
        # self.scroll()
        item_links = self.extract_item_links()
        item_infos = self.extract_item_infos(item_links)
        print(item_infos) # debug
        return item_infos

    def stop(self):
        self.driver.close()
