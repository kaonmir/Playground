"""
# run.py
이 파일은 Celery에게 명령을 내리는 producer입니다.
이 파일 이외의 모듈은 모두 RabbitMQ와 연동하여 실제 프로세스를 구동하는 consumer입니다.

Task를 엮은 workflow는 producer/consumer 어디에나 작성할 수 있습니다.
여기서는 proudcer 단에서 구현하여 봅시다.
"""

from celery import group
from tasks.calc import add
from tasks.email import notify
from tasks.log import log_message

links = add.s(3, 2) | group(notify.s() | log_message.s())
links()
