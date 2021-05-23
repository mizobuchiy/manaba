#!/usr/bin/env python
# coding: utf-8

from dotenv import load_dotenv
from os import getenv
import requests

from selenium_crawler import SeleniumCrawler
from manaba_crawler import ManabaCrawler

def main():

    manaba_crawler = ManabaCrawler(sleep_time=0.5, headless=True)

    load_dotenv()
    all_task = manaba_crawler.exec(
        getenv("HOME_URL"),
        getenv("LOGIN_ID"),
        getenv("LOGIN_PASS"),
        getenv("LOGIN_BTN_XPATH"),
        getenv("TESTS_URL"),
        getenv("SURVEYS_URL"),
        getenv("ASSIGNMENTS_URL"))

    tasks = '◆'
    for task in all_task.split('\n'):
        if(task[:3] == "End"):
            tasks += (task[4:] + "\n◆")
        else:
            tasks += (task + " ")
    tasks = tasks[:-1]


    lst_task = []
    for task in tasks.split('\n'):
        lst_task.append(task + '\n')
    lst_task.sort(key=lambda x: x[-16:])

    message = '\n'
    message += "".join(lst_task)

    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + getenv("TOKEN")}
    send_dic = {'message': message}

    requests.post(getenv("api_url"), headers=TOKEN_dic, data=send_dic)

if __name__ == '__main__':
    main()
