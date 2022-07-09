#!/usr/bin/python3

from cProfile import run
import contextlib


def stop_database():
    pass


def start_database():
    pass


# 1번 방법
class DBHandler:
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, exc_value, trace):
        start_database()


def db_backup():
    run("pg_dump databse")


# 2번 방법
@contextlib.contextmanager
def db_handler():
    stop_database()
    yield
    start_database()


# 3번 방법
class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()

    def __exit__(self, exc_type, exc_value, trace):
        start_database()


@dbhandler_decorator()
def offline_backup():
    run("pg_dump database")


def main():
    with DBHandler:
        db_backup()

    with db_handler():
        db_backup()

    offline_backup()

    pass


if __name__ == "__main__":
    main()
