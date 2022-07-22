from celery_app import celery, smtp_gmail
from email.message import EmailMessage


@celery.task
def notifyToEmailFromResult(result: int):
    msg = EmailMessage()
    msg["Subject"] = "제목입니다."
    msg.set_content(f"{str(result)}가 정답입니까?")
    msg["From"] = "thswpvm1111@gmail.com"
    msg["To"] = "sonjeff@naver.com"

    smtp_gmail.send_message(msg)

    return -143
