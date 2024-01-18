from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Crawling:
    def __init__(self):
        self.url = "https://fruitsfamily.com/discover"
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.item_links = []

    def extract_item_link(self) -> list:
        datas = self.driver.find_elements(By.CLASS_NAME, "CardDeck-item")
        item_links = []
        for i in datas:
            item = i.find_element(By.CLASS_NAME, "ProductPreview")
            self.item_links.append(item.get_attribute("href"))
        return item_links


    def extract_item_infos(self, item_links: list) -> tuple:
        for i in item_links:
            category = self.driver.find_element()
            brand = self.driver.find_element()
            product = self.driver.find_element()
            price = self.driver.find_element()
        return category, brand, product, price

    def crawl(self):
        item_links = self.extract_item_link()
        item_infos = self.extract_item_infos(item_links)


    def stop(self):
        self.driver.close()