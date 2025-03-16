from celery import shared_task
from django.core.mail import send_mail
from time import sleep
from django.conf import settings


@shared_task
def sendEmail():
    sleep(3)
    print("done sending email")
