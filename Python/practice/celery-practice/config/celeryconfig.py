import os


RABBITMQ_URL = os.getenv("RABBITMQ_URL")
if RABBITMQ_URL is None:
    raise Exception("Please set RABBITMQ_URL environment variable.")


main = "son_tasks"
broker = RABBITMQ_URL
backend = "rpc://"
include = ["tasks.calc", "tasks.email", "tasks.log"]
