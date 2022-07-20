from random import randint
import time
from son_app import app
import smtplib


@app.task
def notify(message):
    time.sleep(randint(1, 5))
