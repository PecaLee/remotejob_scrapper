from scrapper import job_db
from save_file import save_to_file
from flask import Flask, render_template, request, send_file, redirect

app = Flask("remoteJobScrapper")

db = {}


@app.route("/")
def root_page():
    return render_template("search.html")


@app.route("/result")
def result_page():
    keyword = request.args.get("searchJobs").lower()
    try:
        if keyword not in db:
            search_db = job_db(keyword)
            db[keyword] = search_db
        results = db[keyword]
    except AttributeError:
        results = None

    return render_template("result.html", results=results, keyword=keyword)


@app.route("/export")
def export():
    keyword = request.args.get("searchJobs").lower()
    try:
        if keyword in db:
            save_to_file(db[keyword], keyword)
            return send_file(f"{keyword}_remotejob.csv", as_attachment=True, attachment_filename=f"{keyword}_remotejob.csv")
        else:
            raise ValueError
    except ValueError:
        return redirect("/")


app.run()
