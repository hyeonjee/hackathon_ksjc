from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from django.http import HttpResponse
import random, requests, pdb, ast, json

# Create your views here.
def create_comment(request, content_id):
    if request.method == "POST":
        content = ast.literal_eval(request.POST.get('content'))
        message = request.POST.get('message')
        identity = content['identity'] 
        # current_user = "익명"
        # comment_content = request.POST.get('content')
        # comment = Comment.objects.create(text=message)
        context = {
            'content': content,
            'message': message,
            'identity': identity,
        }
    return HttpResponse(json.dumps(context), content_type="application/json")