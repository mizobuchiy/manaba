from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import time


class SeleniumCrawler:
    def __init__(self, *, sleep_time=1.0, headless=True):
        self.sleep_time = sleep_time

        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-setuid-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--headless') if headless else None

        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)

        # Sets the amount of time to wait for a page load to complete before
        # throwing an error.
        self.driver.set_page_load_timeout(15)
        # Set the amount of time the driver should wait when searching for
        # elements.
        self.driver.implicitly_wait(15)
        # Sets the amount of time to wait for an asynchronous script to finish
        # execution before throwing an error.
        self.driver.set_script_timeout(15)

    def crawl(self, url):
        self.sleep_before_crawl()
        self.driver.get(url)

    def sleep_before_crawl(self):
        time.sleep(self.sleep_time)

    def get_title(self, url):
        self.crawl(url)
        return self.driver.title

    def get_html(self, url):
        self.crawl(url)
        return self.current_page_html()

    def current_page_html(self):
        html = self.driver.execute_script(
            "return document.getElementsByTagName('html')[0].outerHTML")
        return html

    def send_value(self, css_selector, value):
        javascript_statement = f"""document.querySelector('{css_selector}').value = '{value}'"""
        self.driver.execute_script(javascript_statement)

    def query_click(self, css_selector):
        self.sleep_before_crawl()
        javascript_statement = f"""document.querySelector('{css_selector}').click()"""
        self.driver.execute_script(javascript_statement)
