from son_app import app


@app.task
def log_message(log):
    """
    들어오는 메시지를 포장해 S3로 보낸다.
    파일의 이름은 현재 시간으로 한다.
    내용은 단순히 숫자 하나로 한다.

    :param message: the message to log
    """
    pass
