"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

import os
import requests
from bs4 import BeautifulSoup

os.system("cls")

keyword = input("input keyword").lower()

stack_url = f"https://stackoverflow.com/jobs?r=true&q={keyword}"
wework_url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
remoteok_url = f"https://remoteok.io/remote-dev+{keyword}-jobs"


def stack_scrapper():
    load = requests.get(stack_url)
    soup = BeautifulSoup(load, "html.parser")
    print(soup)


stack_scrapper()
