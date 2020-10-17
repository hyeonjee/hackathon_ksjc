from django.urls import path
from .views import *

app_name = "comments"   
   
urlpatterns = [
    path('<int:content_id>/create_comment/', create_comment, name="create_comment" ),
]
