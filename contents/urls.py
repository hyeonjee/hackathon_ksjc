from django.urls import path
from .views import *

app_name = "contents"

urlpatterns = [
    path('', show, name="contents"),
    path('<int:content_id>/create_comment/', create_comment, name="create_comment" ),

]



