from django.http import HttpResponse, JsonResponse
from .tasks import sendEmail
from django.core.cache import cache
import requests


def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Email sent</h1>")


def test(request):
    if cache.get("test_delay_api") is None:
        response = requests.get(
            "https://fbe7e2ba-0dd7-498f-8c09-da15de86097d.mock.pstmn.io/test/delay/5"
        )
        cache.set("test_delay_api", response.json())
    return JsonResponse(cache.get("test_delay_api"))
