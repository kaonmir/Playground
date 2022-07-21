# tasks.py
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
