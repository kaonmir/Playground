from celery import Celery
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

RABBITMQ_URL = os.getenv("RABBITMQ_URL")
if RABBITMQ_URL is None:
    raise Exception("Please set RABBITMQ_URL environment variable.")


app = Celery(
    "son_tasks",
    broker=RABBITMQ_URL,
    backend="rpc://",
    include=["tasks.calc", "tasks.email", "tasks.log"],
)

smtp_gmail = smtplib.SMTP("smtp.gmail.com", 587)
smtp_gmail.ehlo()
smtp_gmail.starttls()
smtp_gmail.login("thswpvm1111@gmail.com", "wajiruayokplkhzm")
