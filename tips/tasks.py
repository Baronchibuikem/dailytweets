from django.core.mail import EmailMessage
from celery.utils.log import get_task_logger
from dailytips.celery import app
from tips.models import DailyTip



logger = get_task_logger(__name__)



@app.task
def get_daily_tips():
    logger.info("Starting job")
    new_tweet = DailyTip(
        "python_tip": "value",
        "link": "value",
        "posted_by" : "value",
        "published": "value",
        "timestamp": "value"
    )
    new_tweet.save()
    logger.info("New tweet has been saved to the database")
    return new_tweet