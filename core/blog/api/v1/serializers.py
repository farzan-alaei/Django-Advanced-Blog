from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    status = serializers.BooleanField()
    category = serializers.CharField()
    created_date = serializers.DateTimeField()
    updated_date = serializers.DateTimeField()
    published_date = serializers.DateTimeField()