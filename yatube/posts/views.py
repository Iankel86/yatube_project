#  from django.shortcuts import HttpResponse
from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group
# Все функции прописаны в posts/urls.py


# Главная страница   (http://127.0.0.1:8000/)

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

# Страница с биографией    (http://127.0.0.1:8000/group_list/)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
