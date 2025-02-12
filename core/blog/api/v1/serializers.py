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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField()
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "author",
            "category",
            "content",
            "snippet",
            "relative_url",
            "absolute_url",
            "status",
            "created_date",
            "published_date",
        ]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.get_absolute_api_url())

    def to_representation(self, instance):
        return super().to_representation(instance)
