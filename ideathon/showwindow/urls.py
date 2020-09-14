from django.urls import path
from django.conf.urls import url, include
from .views import main

app_name = "showwindow"

urlpatterns = [
    path('', main, name="main"),
]