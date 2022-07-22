#!/usr/bin/python3

from flask import (
    Flask,
    flash,
    message_flashed,
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
        number1 = request.form["number1"]
        number2 = request.form["number2"]

        if not number1:
            flash("Number1 is required!")
        elif not number2:
            flash("Number2 is required!")
        else:
            # | Signature("tasks.notificate.notifyToEmailFromResult")
            celery.send_task(
                name="tasks.calc.add",
                args=[int(number1), int(number2)],
                chain=[Signature("tasks.notificate.notifyToEmailFromResult")],
            )
            return redirect(url_for("about"))

    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
