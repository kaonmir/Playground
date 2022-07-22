from celery_app import celery, smtp_gmail
from email.message import EmailMessage


@celery.task
def emailNotionItemAdded(message):
    msg = EmailMessage()
    msg["Subject"] = "Notion Item is added to database"
    msg.set_content(f"{str(message)}")
    msg["From"] = "thswpvm1111@gmail.com"
    msg["To"] = "sonjeff@naver.com"

    smtp_gmail.send_message(msg)
    return -143
