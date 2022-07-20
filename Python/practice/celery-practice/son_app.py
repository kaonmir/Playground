from celery import Celery

app = Celery(
    "son_tasks",
    broker="amqp://son:son@192.168.25.40:5672//",
    backend="rpc://",
    include=["tasks.calc", "tasks.email", "tasks.log"],
)
