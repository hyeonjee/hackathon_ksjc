from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import random, requests, pdb, ast, json

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
        identity = data['identity']
        attr_name = data['attraction']
        attr_img = data['image'][0]['url']
        # wrap by class
        context = {
        'data':data,
        'name':attr_name,
        'identity': identity,
        'img':attr_img,
        'place':'실내3층',#dump1
        'explanation':'대한민국의 국민이 되는 요건은 법률로 정한다. 모든 국민은 인간으로서의 존엄과 가치를 가지며, 행복을 추구할 권리를 가진다. 국가는 개인이 가지는 불가침의 기본적 인권을 확인하고 이를 보장할 의무를 진다.', #dump2
        }   
        
    return render(request, 'contents/response.html', context)

# 이거 설마 Content가 없어서 그런건가, 그 Content모델이 있기는 해도 api로 불러온 data만 있지 Content에 저장은 안 되어 있잖아 그래서 그런건가? comment에 저장할 때는 content 객체의 정보가 필요한데 그걸 우리가 임의로
# 그냥 data 불러온걸 넣어준거잖아
# 만약 comment를 content 없이 넣고 싶으면 comment 앱을 하나 새로 파서 거기에 넣는게 좋은 것 같은데
# 만약 content에서도 사용하고 싶으면 show.html에서 데이터를 불러올 때, 데이터를 Content 모델에 다 저장해줘야 함. ㅋㅋㅋㅋㅋ 그러면 앱 만들어서 한 번 해 봐
# 우선 해봐 ㄲ, 해보고 막히면 도와줄게 라이브쉐어는 안 꺼놓고 다른거 하고 있을테니까 필요하면 카톡으로 연락 ㄱ
#있을때도 이랬는데... 그건 아니지 않을까?? Content랑 따로 움직이니까 ㅇㅇ 그치그치 Content는 일단 지웠어  holly fuck 그러면 일단 content에 있는 model은 필요없게 되는거네?

#아 그러면 앱을 따로 만드는게 뭔가 더 쉬울거 같다 떙큐때윸넹넹