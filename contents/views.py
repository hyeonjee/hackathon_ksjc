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
        # handle structure
        data = datas['records'][num]['fields']
        identity = data['identity']
        attr_name = data['attraction']
        attr_img = data['image'][0]['url']
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
            'place':'실내3층',#dump1
            'explanation':'대한민국의 국민이 되는 요건은 법률로 정한다. 모든 국민은 인간으로서의 존엄과 가치를 가지며, 행복을 추구할 권리를 가진다. 국가는 개인이 가지는 불가침의 기본적 인권을 확인하고 이를 보장할 의무를 진다.', #dump2
            'listVar':comments 
        }
       
    return render(request, 'contents/response.html', content)

def postComment(request):
    '''TBD'''

