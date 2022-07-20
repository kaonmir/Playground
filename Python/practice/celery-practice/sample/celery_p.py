#!/usr/bin/python3

from celery_c import add

print(add.delay(300, 10))
