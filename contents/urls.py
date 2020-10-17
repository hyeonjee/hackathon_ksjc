from django.urls import path
from .views import *

app_name = "contents"

urlpatterns = [
    path('', show, name="contents"),
]



