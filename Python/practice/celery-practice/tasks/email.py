from random import randint
import time
from son_app import app


@app.task
def notify():
    time.sleep(randint(1, 5))
