# Create your tasks here
from datetime import datetime
from celery import shared_task
from time import sleep
from django.core.mail import send_mail
import os
from decouple import config


@shared_task
def send_mail_task(to):
    send_mail(
        'Hello, from Celery',
        "Welcome to Django-Company, New account created.",
        "anubhav.edcjss@gmail.com",
        [to],
        fail_silently=False,
    )
    print("Mail sent successfully.")
    return None
