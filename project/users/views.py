from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def mypage(request):
    posts = Post.objects.filter(writer=request.user)
    return render(request, 'users/mypage.html', {'posts': posts})

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'main/detail.html', {'post':post})