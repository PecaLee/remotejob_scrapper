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


def make_soup(url):
    load = requests.get(url)
    soup = BeautifulSoup(load.content, "html.parser")
    return soup


def remoteok_scrapper(keyword):
    remoteok_url = f"https://remoteok.io/remote-dev+{keyword}-jobs"
    db = []
    remoteok = "https://remoteok.io"
    soup = make_soup(remoteok_url)
    table = soup.find("table", {"id": "jobsboard"})
    results = table.find_all("tr", {"class": "job"})
    for result in results:
        job_title = result.select(
            ".company.position.company_and_position h2")[0].text
        job_link = result.find("a", {"class": "preventLink"}).get("href")
        company = result.select(".companyLink h3")[0].text

        jobs = {
            "title": job_title,
            "company": company,
            "link": remoteok + job_link
        }

        db.append(jobs)

    return db


def stack_scrapper(keyword):
    stack_url = f"https://stackoverflow.com/jobs?r=true&q={keyword}"
    db = []
    stack = "https://stackoverflow.com"
    soup = make_soup(stack_url)
    list_results = soup.find("div", {"class": "listResults"})
    results = list_results.find_all("div", {"class": "fl1"})
    for result in results:
        job = result.find("a", {"class": "s-link"})
        job_title = job.text
        job_link = job.get("href")
        company = result.select("h3 span:first-child")[0].text.strip()

        jobs = {
            "title": job_title,
            "company": company,
            "link": stack + job_link
        }

        db.append(jobs)

    return db


def wework_scrapper(keyword):
    wework_url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
    db = []
    wework = "https://weworkremotely.com"
    soup = make_soup(wework_url)
    job_container = soup.find("div", {"id": "job_list"})
    list_results = job_container.find("section", {"id": "category-2"})
    results = list_results.find_all("li", {"class": "feature"})
    for result in results:
        job_title = result.find("span", {"class": "title"}).text
        job_link = result.find("div", {"class": "tooltip"})
        if job_link == None:
            job_link = result.find("a").get("href")
        else:
            job_link = result.select(".tooltip ~ a")[0].get("href")
        company = result.find("span", {"class": "company"}).text

        jobs = {
            "title": job_title,
            "company": company,
            "link": wework + job_link
        }

        db.append(jobs)

    return db


def job_db(keyword):
    db = remoteok_scrapper(keyword) + \
        stack_scrapper(keyword) + wework_scrapper(keyword)
    return db
