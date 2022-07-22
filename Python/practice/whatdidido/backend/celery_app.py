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
NOTION_DATABASE_TOKEN = os.getenv("NOTION_DATABASE_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
if NOTION_DATABASE_TOKEN is None or NOTION_DATABASE_ID is None:
    raise Exception(
        "Please set NOTION_DATABASE_TOKEN and NOTION_DATABASE_ID environment variables."
    )

celery = Celery(
    "tasks",
    broker=RABBITMQ_URL,
    backend="rpc://",
    include=["tasks.calc", "tasks.notificate", "tasks.notion"],
)

import smtplib

smtp_gmail = smtplib.SMTP("smtp.gmail.com", 587)
smtp_gmail.ehlo()
smtp_gmail.starttls()
smtp_gmail.login(GMAIL_ADDRESS, GMAIL_CREDENTIAL)


token = NOTION_DATABASE_TOKEN
databaseId = NOTION_DATABASE_ID

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13",
}
