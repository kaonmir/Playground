import time
from son_app import app


@app.task
def calculate(x, y):
    time.sleep(3)
    return x + y


@app.task
def callback(results):
    return results
