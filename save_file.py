import csv
from scrapper import job_db


def save_to_file(db, keyword):
    db = db
    file = open(f"{keyword}_remotejob.csv", mode="w", encoding="utf-8")
    jobwriter = csv.writer(file)
    jobwriter.writerow(["job", "company", "link"])
    for job in db:
        jobwriter.writerow(list(job.values()))
    return
