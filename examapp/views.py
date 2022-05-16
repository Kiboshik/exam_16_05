from django.shortcuts import render
from rest_framework import viewsets, response, views, status
from .models import Post, Comments, Likes
from .serializer import PostSerializer, CommentsSerializer, LikesSerializer, UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class UserRegisterAPIViews(views.APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]


class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    permission_classes = [IsAuthenticated]
