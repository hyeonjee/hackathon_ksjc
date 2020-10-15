from django.shortcuts import render, redirect, get_object_or_404
from .models import Content, Comment
import random, requests

# AirTable DataLoad

def show(request):
    # load data by request
    url = 'https://api.airtable.com/v0/appLevy8PRRITJAAt/Imported%20table?api_key=keyizI5yDulohm113'
    datas = requests.get(url)
    if datas.status_code == 200:
        datas = datas.json()
        # make random variable
        num = random.randint(0,20)
        # handle structure
        data = datas['records'][num]['fields']
        attr_name = data['attraction']
        attr_img = data['image'][0]['url']
        # wrap by class
        content = {
        'data':data,
        'name':attr_name,
        'img':attr_img,
        'place':'실내3층',#dump1
        'explanation':'대한민국의 국민이 되는 요건은 법률로 정한다. 모든 국민은 인간으로서의 존엄과 가치를 가지며, 행복을 추구할 권리를 가진다. 국가는 개인이 가지는 불가침의 기본적 인권을 확인하고 이를 보장할 의무를 진다.', #dump2
        }
        return render(request, 'contents/response.html', {'contents':content})

# Comment

def create_comment(request, content_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=content_id)
        current_user = request.user
        comment_content = request.POST.get('content')
        Comment.objects.create(content=comment_content, writer=current_user, post=post)
    return redirect('contents:get_random', content_id)
    
