#!/usr/bin/python3

from flask import Flask
from celery import Celery

import os
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_URL = os.getenv("RABBITMQ_URL")
if RABBITMQ_URL is None:
    raise Exception("Please set RABBITMQ_URL environment variable.")


celery = Celery(
    "tasks",
    broker=RABBITMQ_URL,
    backend="rpc://",
    include=["tasks.calc"],  # ["tasks.calc", "tasks.email", "tasks.log"]
)


app = Flask(__name__)


@app.route("/")
def hello_world():
    celery.send_task("tasks.calc.add", (2, 109000000))
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
