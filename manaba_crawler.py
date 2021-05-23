#!/usr/bin/env python
# coding: utf-8

# import requests
# import chromedriver_binary
# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from time import sleep
# from dotenv import load_dotenv
# from os import getenv
# from webdriver_manager.chrome import ChromeDriverManager

from selenium_crawler import SeleniumCrawler


class ManabaCrawler(SeleniumCrawler):
    def __init__(self, **args):
        super().__init__(**args)

    def login(self, login_id, login_pass, login_btn_xpath):
        self.driver.find_element_by_id(
            "username_input").send_keys(login_id)
        self.driver.find_element_by_id("password_input").send_keys(login_pass)
        self.sleep_before_crawl()
        self.driver.find_element_by_xpath(
            login_btn_xpath).send_keys(Keys.ENTER)
        self.sleep_before_crawl()

    def get_tasks(self, url):
        self.crawl(url)
        element = self.driver.find_element_by_xpath(
            '/html/body/div[3]/section/ul')
        return element.text

    def get_alltask(self, tests_url, surveys_url, assignments_url):
        all_task = ''
        all_task += self.get_tasks(tests_url)
        all_task += "\n"
        all_task += self.get_tasks(surveys_url)
        all_task += "\n"
        all_task += self.get_tasks(assignments_url)
        return all_task

    def quit_crawler(self):
        self.driver.quit()

    def exec(
            self,
            home_url,
            login_id,
            login_pass,
            login_btn_xpath,
            tests_url,
            surveys_url,
            assignments_url):

        _ = self.crawl(home_url)

        self.login(login_id, login_pass, login_btn_xpath)

        all_task = self.get_alltask(tests_url, surveys_url, assignments_url)

        self.quit_crawler()

        return all_task

