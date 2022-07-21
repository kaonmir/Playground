#!/usr/bin/python3

from flask import Flask
from celery import Celery


celery = Celery(
    "tasks",
    broker="amqp://son:son@192.168.25.40:5672//",
    backend="rpc://",
    include=["tasks.calc"],  # ["tasks.calc", "tasks.email", "tasks.log"]
)


app = Flask(__name__)


@app.route("/")
def hello_world():
    celery.send_task("tasks.calc.add", (2, 109000000))
    return "Hello World!"


if __name__ == "__main__":
    app.run()
