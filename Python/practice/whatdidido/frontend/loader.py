import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_URL = os.getenv("RABBITMQ_URL")
if RABBITMQ_URL is None:
    raise Exception("Please set RABBITMQ_URL environment variable.")

HOST = os.getenv("HOST")
if HOST is None:
    raise Exception("Please set HOST environment variable.")
PORT = os.getenv("PORT")
if PORT is None:
    raise Exception("Please set PORT environment variable.")


celery = Celery(
    "tasks",
    broker=RABBITMQ_URL,
    backend="rpc://",
    include=["tasks.calc", "tasks.notificate", "tasks.notion"],
)
