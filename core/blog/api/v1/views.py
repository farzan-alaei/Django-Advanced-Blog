from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer
from blog.models import Post


@api_view(["GET"])
def postList(request):
    return Response("ok")


@api_view(["GET"])
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)
