from son_app import app


@app.task
def log_message(message):
    print(message)
    return message
