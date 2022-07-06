#!/usr/bin/python3

import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def blocking_lock(lock):
    logging.debug("Start blocking lock")

    while True:
        time.sleep(1)
        lock.acquire()
        try:
            logging.debug("Grab it")
            time.sleep(0.5)
        finally:
            logging.debug("Release")
            lock.release()

        # with lock:
        #     logging.debug("Grab it")
        #     time.sleep(0.5)
        #     logging.debug("Release")


def nonblocking_lock(lock):
    logging.debug("Start nonblocking lock")

    attempt, grab = 0, 0
    while grab < 3:
        time.sleep(1)
        logging.debug("Attempt")
        success = lock.acquire(False)

        try:
            attempt += 1
            if success:
                logging.debug("Grab it")
                grab += 1
        finally:
            if success:
                logging.debug("Release")
                lock.release()
    logging.debug("Attempt: %s, grab: %s" % (attempt, grab))


def main():
    lock = threading.Lock()

    blocking = threading.Thread(
        name="blocking", target=blocking_lock, args=(lock,))
    blocking.setDaemon(True)
    blocking.start()

    nonblocking = threading.Thread(
        name="nonblocking", target=nonblocking_lock, args=(lock,))
    nonblocking.start()


if __name__ == "__main__":
    main()
