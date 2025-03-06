import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
class TestPostAPI:
    def test_get_post_response_200_status(self):
        client = APIClient()
        url = reverse("blog:api-v1:post-list")
        response = client.get(url)
        assert response.status_code == 200
