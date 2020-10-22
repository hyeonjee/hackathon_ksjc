from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from django.http import HttpResponse
import random, requests, pdb, ast, json
import logging

# for console log
logger = logging.getLogger(__name__)

logger.error("something wrong")

# data post by REST API
def create_comment(request, content):
    if request.method == "POST":
        content = ast.literal_eval(request.POST.get('content'))
        message = request.POST.get('message')
        identity = content['identity']