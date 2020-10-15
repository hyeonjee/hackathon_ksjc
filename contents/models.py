from django.db import models
import requests, json, random
from django.contrib.auth.models import User

# Content
# We don't use content model now.
# because we use api directly, without saving to our own db.

class Content(models.Model):
    content = models.TextField()
    members = models.IntegerField(default = 0)
    place = models.IntegerField(default = 0)
    doing = models.IntegerField(default = 0)
    kinds = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.TextField()

# Comment

class Comment(models.Model):
    text = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)