from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Post, Comment, Media
from .serializers import PostSerializer, CommentSerializer, MediaSerializer


class PostListCreateApi(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CommentListCreateApi(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class MediaListCreateApi(ListCreateAPIView):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
class MediaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()

