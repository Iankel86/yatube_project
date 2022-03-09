from django.shortcuts import HttpResponse
from django.shortcuts import render

# Главная страница


def index(request):
#    return HttpResponse('Главная страница')
    template = 'posts/index.html'
    return render(request, template)

# Страница с постами


def group_posts(request, slug):
    return HttpResponse('Страница с постом после фильтра по группе')