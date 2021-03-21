from django.core.mail import EmailMessage
from celery.utils.log import get_task_logger
from dailytips.celery import app



logger = get_task_logger(__name__)



@app.task
def send_reminder():
    club = {
        "1" : "barcelona",
        "2": "chelsea",
        "3": "PSG"
    }
    logger.info("Starting job")
    return club