import pytest
from datetime import datetime
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestPostAPI:
    client = APIClient()

    def test_get_post_response_200_status(self):
        url = reverse("blog:api-v1:post-list")
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "test",
            "status": True,
            "published_date": datetime.now(),
        }
        response = self.client.post(url, data)
        assert response.status_code == 401