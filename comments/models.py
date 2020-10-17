from django.db import models
import requests, json, random
from django.contrib.auth.models import User

# Content
# We don't use content model now.
# because we use api directly, without saving to our own db.

# Comment
class Comment(models.Model):
    identity = models.IntegerField(default = 0)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)