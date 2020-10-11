from django.db import models
import requests, json, random
    
# Create your models here.
class Content(models.Model):
    content = models.TextField()
    members = models.IntegerField(default = 0)
    place = models.IntegerField(default = 0)
    doing = models.IntegerField(default = 0)
    kinds = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.TextField()

#에어테이블 데이터 Content에 저장하기
url = 'https://api.airtable.com/v0/appLevy8PRRITJAAt/Imported%20table?api_key=keyizI5yDulohm113'
data = requests.get(url).json()
data_list = data['records']
attraction_list= [] 
img_url_list = []
for i in range(0,len(data_list)):
    data = data_list[i]['fields']
    attraction = data['attraction']
    img_url = data['image'][0]['url']
    attraction_list.append(attraction)
    img_url_list.append(img_url)
    post = Content(content = attraction_list[i], photo = img_url_list[i])
    post.save()

