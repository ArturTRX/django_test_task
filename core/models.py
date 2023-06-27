from django.db import models


class Post(models.Model):
    user_id = models.IntegerField(default=99999942)
    title = models.CharField(max_length=200)
    body = models.TextField()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
