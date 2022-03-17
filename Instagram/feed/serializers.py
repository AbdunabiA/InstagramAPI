from django.core.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import *

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
