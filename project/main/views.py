from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Post, Comment, Tag

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
    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/detail.html', {'post':post, 'comments': comments})
    
    elif request.method == 'POST':
        new_comment = Comment()

        new_comment.post = post
        new_comment.writer = request.user
        new_comment.content = request.POST['content']
        new_comment.pub_date = timezone.now()

        new_comment.save()
        return redirect('main:detail', id)

def edit(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {'post' : edit_post})

def update(request, id):
    update_post = Post.objects.get(pk=id)
    if request.user.is_authenticated and request.user == update_post.writer:
        update_post.title = request.POST.get('title')
        update_post.email = request.POST.get('email')
        update_post.body = request.POST.get('body')
        update_post.pub_date = timezone.now()

        if request.FILES.get('image'):
            update_post.image = request.FILES['image']
        
        update_post.save()
        return redirect('main:detail', update_post.id)
    return redirect('main:detail', update_post.id) 

def delete(request, id):
    delete_post = Post.objects.get(pk=id)
    delete_post.delete()
    return redirect('main:secondpage')

def deleteComment(request, id):
    delete_comment = Comment.objects.get(pk=id)
    post = Post.objects.get(pk=delete_comment.post.id)
    delete_comment.delete()

    return redirect('main:detail',post.id)

def create(request):
    new_post = Post()

    new_post.title = request.POST.get('title')
    new_post.writer = request.user
    new_post.email = request.POST.get('email')
    new_post.body = request.POST.get('body')
    new_post.pub_date = timezone.now()
    new_post.image = request.FILES.get('image')


    new_post.save()

    words = new_post.body.split(' ')
    tag_list = []

    for w in words:
        if len(w)>0:
            if w[0] == '#':
                tag_list.append(w[1:])

    for t in tag_list:
        tag, boolean = Tag.objects.get_or_create(name=t)
        new_post.tags.add(tag.id)

    return redirect('main:detail', new_post.id) 

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'main/tag-list.html', {'tags' : tags })

def tag_posts(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = tag.posts.all()
    return render(request, 'main/tag-post.html', {
        'tag' : tag,
        'posts' : posts
    })