from django.db import models

# Create your models here.
class Content(models.Model):
    content = models.TextField()
    members = models.IntegerField(default = 0)
    place = models.IntegerField(default = 0)
    doing = models.IntegerField(default = 0)
    kinds = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True, null=True)