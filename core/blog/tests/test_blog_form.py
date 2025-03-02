from datetime import datetime
from django.test import TestCase

from ..forms import PostForm
from ..models import Category


class TestPostForm(TestCase):

    def test_post_form_with_valid_data(self):
        category_obj = Category.objects.create(name="hello")
        form = PostForm(
            {
                "title": "test",
                "content": "description",
                "status": True,
                "category": category_obj,
                "published_date": datetime.now(),
            }
        )
        self.assertTrue(form.is_valid())

    def test_post_form_with_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
