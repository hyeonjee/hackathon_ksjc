from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import random, requests, pdb, ast, json

# AirTable DataLoad
def show(request, id):
    # load data by request
    url = 'https://api.airtable.com/v0/appLevy8PRRITJAAt/Attraction?api_key=keyizI5yDulohm113'
    datas = requests.get(url)
    if datas.status_code == 200:
        datas = datas.json()
        # make random variable
        num = id
        # check    
        if 'value' in request.GET:
            if request.GET.get('value')=='999':
                num = random.randint(0,51)
        # handle structure
        data = datas['records'][num]['fields']
        identity = data['identity']
        attr_name = data['attraction']
        attr_img = data['image'][0]['url']
        place = data['place']
        explanation = data['explanation']
        if 'Comment' in data:
            comments = data['Comment'] # This is comments(list)
        else : 
            comments = None
        # wrap by class(x), dictionary(o)
        content = {
            'data':data,
            'name':attr_name,
            'identity': identity,
            'img':attr_img,
            'place':place,#dump1
            'explanation': explanation, #dump2
            'listVar':comments 
        }
    return render(request, 'contents/response.html', content)


def postComment(request):
    comment = request.GET.get('q')
    id = request.GET.get('p')
    return redirect('contents:show', id)