import os
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_URL = os.getenv("RABBITMQ_URL")
if RABBITMQ_URL is None:
    raise Exception("Please set RABBITMQ_URL environment variable.")


broker_url = RABBITMQ_URL
backend = "rpc://"
# task_routes = {"task_name": {"queue": "sony_tasks"}}

include = ["tasks.calc", "tasks.email", "tasks.log"]
