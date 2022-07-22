#!/usr/bin/python3

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from loader import celery, HOST, PORT
from celery import Signature

app = Flask(__name__)
app.config["SECRET_KEY"] = "asfjpbiowe9237nkl"


@app.route("/", methods=("GET", "POST"))
def hello_world():
    if request.method == "POST":
        restaurant = request.form["restaurant"]
        menu = request.form["menu"]

        # | Signature("tasks.notificate.notifyToEmailFromResult")
        celery.send_task(
            name="tasks.notion.createNotionItemToDatabase",
            args=[restaurant, menu],
            chain=[Signature("tasks.notificate.emailNotionItemAdded")],
        )
        return redirect(url_for("about"))

    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
