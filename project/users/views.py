from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def mypage(request):
    posts = Post.objects.filter(writer=request.user)
    return render(request, 'users/mypage.html', {'posts': posts})
