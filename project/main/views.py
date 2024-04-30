from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Post

# Create your views here.

def mainpage(request):
    context = {
        'members': ['url', '반복문', '조건문'],
        'info':{'model': 'DB와 상호작용 담당', 'template': '사용자와 상호작용 담당', 'view': '웹 서비스 내부 동작의 논리를 담당'}
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    posts = Post.objects.all()
    return render(request, 'main/secondpage.html', {'posts': posts})


def new_post(request):
    return render(request, 'main/new-post.html')

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'main/detail.html', {'post':post})

def edit(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {'post' : edit_post})

def update(request, id):
    update_post = Post.objects.get(pk=id)

    update_post.title = request.POST.get('title')
    update_post.writer = request.POST.get('writer')
    update_post.email = request.POST.get('email')
    update_post.body = request.POST.get('body')
    update_post.pub_date = timezone.now()
    update_post.image = request.FILES.get('image')

    if request.FILES.get('image'):
        update_post.image = request.FILES['image']

    update_post.save()

    return redirect('main:detail', update_post.id) 

def delete(request, id):
    delete_post = Post.objects.get(pk=id)
    delete_post.delete()
    return redirect('main:secondpage')

def create(request):
    new_post = Post()

    new_post.title = request.POST.get('title')
    new_post.writer = request.POST.get('writer')
    new_post.email = request.POST.get('email')
    new_post.body = request.POST.get('body')
    new_post.pub_date = timezone.now()
    new_post.image = request.FILES.get('image')


    new_post.save()

    return redirect('main:detail', new_post.id) 