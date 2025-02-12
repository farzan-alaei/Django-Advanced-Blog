from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)
from .serializers import PostSerializer
from blog.models import Post
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

"""
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
"""

"""
@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response(
            {"detail": "item deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
"""

'''
class PostList(APIView):
    """
    getting a list of posts and creating new posts
    """

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        """
        retrieve a list of posts
        """
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        creating a post with provided data
        """
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''


class PostList(ListCreateAPIView):
    """
    getting a list of posts and creating new post
    """

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


'''
class PostDetail(APIView):
    """
    getting a single post
    """

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_object(self, id):
        """
        getting a single post
        """
        return get_object_or_404(Post, pk=id, status=True)

    def get(self, request, id):
        post = self.get_object(id)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, id):
        """
        updating a post
        """
        post = self.get_object(id)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        """
        deleting a post
        """
        post = self.get_object(id)
        post.delete()
        return Response(
            {"detail": "item deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
'''


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
