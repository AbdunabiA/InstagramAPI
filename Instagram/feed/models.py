from django.conf import settings
from django.db import models


class Post(models.Model):
    text = models.CharField(max_length=300, blank=True)
    likes = models.ManyToManyField(settings.INSTA_ACCOUNT, related_name='post_likes')
    def __str__(self):
        return f'{self.text}'
class Comment(models.Model):
    text = models.CharField(max_length=300)
    user = models.ForeignKey(settings.INSTA_ACCOUNT, on_delete=models.CASCADE, related_name='post_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.INSTA_ACCOUNT, related_name='comment_likes')
    def __str__(self):
        return f'{self.user} {self.post}'
class Media(models.Model):
    video = models.URLField(blank=True)
    photo = models.URLField(blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)