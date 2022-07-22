# tasks.py
from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_URL = os.getenv("RABBITMQ_URL")
if RABBITMQ_URL is None:
    raise Exception("Please set RABBITMQ_URL environment variable.")
GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_CREDENTIAL = os.getenv("GMAIL_CREDENTIAL")
if GMAIL_ADDRESS is None or GMAIL_CREDENTIAL is None:
    raise Exception(
        "Please set GMAIL_ADDRESS and GMAIL_CREDENTIAL environment variables."
    )


celery = Celery(
    "tasks",
    broker=RABBITMQ_URL,
    backend="rpc://",
    include=["tasks.calc", "tasks.notificate"],
)

import smtplib

smtp_gmail = smtplib.SMTP("smtp.gmail.com", 587)
smtp_gmail.ehlo()
smtp_gmail.starttls()
smtp_gmail.login(GMAIL_ADDRESS, GMAIL_CREDENTIAL)
