from django.shortcuts import render, redirect, get_object_or_404
from .models import Content
import random
# Create your views here.
def get_random(request):
    posts = Content.objects.all()
    post = random.sample(list(posts),1)
    return render(request, 'contents/response.html', {'posts': post})
   


    
    

