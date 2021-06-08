# Create your tasks here

from datetime import datetime
from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def sleepy(d):
    prev = datetime.now().second
    sleep(d)
    tot = datetime.now().second - prev
    return str(tot)


@shared_task
def send_mail_task():
    send_mail(
        'Hello, from Celery',
        "Celery worked obviously.",
        "anubhav.edcjss@gmail.com",
        ["anubhav.edcjss@gmail.com"],
        fail_silently=False
    )
    return None
