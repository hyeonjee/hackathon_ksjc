from django.urls import path
from .views import *

app_name = "contents"

urlpatterns = [
    path('show/<int:id>', show, name="show"),
    path('postComment/', postComment, name="postComment"),
]