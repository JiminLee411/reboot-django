from django.shortcuts import render
from .models import PastLife
from faker import Faker
import requests
from decouple import config

# Create your views here.
def index(request):
    return render(request, 'pastLifes/index.html')

def showpast(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    if not PastLife.objects.filter(name=name, age=age):
        past = PastLife()
        past.name = name
        past.age = age
        fake = Faker('ko_KR')
        past.myjob = fake.job()
        past.save()
    else:
        past = PastLife.objects.get(name=name, age=age)
    # 직업 결과에 따라, giphy 요청
    job = past.myjob
    api_key = config('GIPHY_API_KEY')
    url = f'http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={job}&lang=ko'
    # 2. 요청 보내기
    response = requests.get(url).json()
    # 3. 응답 결과에서 이미지 url 뽑기
    try:
        image_url = response['data'][0].get('images').get('orignal').get('url')
    except:
        image_url = None
    context = {
        'past':past,
        'image_url':image_url,
    }
    return render(request, 'pastLifes/showpast.html', context)


        