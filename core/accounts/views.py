from django.http import HttpResponse, JsonResponse
from .tasks import sendEmail
import requests


def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Email sent</h1>")


def test(request):
    response = requests.get(
        "https://fbe7e2ba-0dd7-498f-8c09-da15de86097d.mock.pstmn.io/test/delay/5"
    )
    return JsonResponse(response.json())
