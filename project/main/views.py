from django.shortcuts import render

# Create your views here.

def mainpage(request):
    context = {
        'members': ['url', '반복문', '조건문'],
        'info':{'model': 'DB와 상호작용 담당', 'template': '사용자와 상호작용 담당', 'view': '웹 서비스 내부 동작의 논리를 담당'}
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    context = {
        'members' : ['슬램덩크', '주로옥', '햐안집']
    }
    return render(request, 'main/secondpage.html', context)