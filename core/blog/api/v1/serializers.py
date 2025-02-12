from rest_framework import serializers
from blog.models import Post, Category

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     status = serializers.BooleanField()
#     category = serializers.CharField()
#     created_date = serializers.DateTimeField()
#     updated_date = serializers.DateTimeField()
#     published_date = serializers.DateTimeField()


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "author",
            "category",
            "content",
            "status",
            "created_date",
            "published_date",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]