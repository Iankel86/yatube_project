from django.shortcuts import HttpResponse
from django.shortcuts import render

# Главная страница


def index(request):
#    return HttpResponse('Главная страница')
    template = 'posts/index.html'
    return render(request, template)

# Страница с постами


def group_posts(request, slug):
    return HttpResponse(f'Страница с постом после фильтра по группе')

def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)
