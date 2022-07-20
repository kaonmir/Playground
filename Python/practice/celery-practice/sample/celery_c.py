from celery import Celery


app = Celery("tasks", broker="amqp://son:son@192.168.25.40:5672/")


@app.task
def add(x, y):
    return x + y
