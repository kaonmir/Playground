from celery_app import celery


@celery.task
def notifyToEmailFromResult(result: int):
    return result
