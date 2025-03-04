from django.test import TestCase
from datetime import datetime
from ..models import Post
from accounts.models import User, Profile


class TestPostModel(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            email="test@test.com", password="a/@123456789"
        )

        self.profile = Profile.objects.create(
            user=self.user, first_name="test", last_name="test", description="test"
        )

    def test_create_post_with_valid_data(self):

        post = Post.objects.create(
            author=self.profile,
            title="Test Post",
            content="This is a test post",
            status=True,
            category=None,
            published_date=datetime.now(),
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEqual(post.title, "Test Post")
