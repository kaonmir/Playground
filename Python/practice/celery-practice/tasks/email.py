from random import randint
import time
from son_app import app, smtp_gmail
from email.message import EmailMessage


@app.task
def notify(message):
    msg = EmailMessage()
    msg["Subject"] = "제목입니다."
    msg.set_content(f"{str(message)}가 정답입니까?")
    msg["From"] = "thswpvm1111@gmail.com"
    msg["To"] = "sonjeff@naver.com"

    smtp_gmail.send_message(msg)

    time.sleep(randint(1, 5))


### 아래는 첨부파일 예시 ###
# file='./test.csv'
# fp = open(file,'rb')
# file_data=fp.read()
# msg.add_attachment(file_data,maintype='text',subtype='plain',filename="test.csv")
