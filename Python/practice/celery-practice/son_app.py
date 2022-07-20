from celery import Celery
import smtplib
from dotenv import load_dotenv
import os
from config import celeryconfig

load_dotenv()

GMAIL_CREDENTIAL = os.getenv("GMAIL_CREDENTIAL")
GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
if GMAIL_CREDENTIAL is None or GMAIL_ADDRESS is None:
    raise Exception(
        "Please set GMAIL_CREDENTIAL and GMAIL_ADDRESS environment variables."
    )

app = Celery()
app.config_from_object(celeryconfig)

smtp_gmail = smtplib.SMTP("smtp.gmail.com", 587)
smtp_gmail.ehlo()
smtp_gmail.starttls()
smtp_gmail.login(GMAIL_ADDRESS, GMAIL_CREDENTIAL)
