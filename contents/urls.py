from django.urls import path
from .views import *

app_name = "contents"

urlpatterns = [
    path('', get_random, name="contents"),
]