#  from django.shortcuts import HttpResponse
from django.shortcuts import render
# Импортируем модель, чтобы обратиться к ней
from .models import Post
# Все функции прописаны в posts/urls.py


# Главная страница   (http://127.0.0.1:8000/)

def index(request):

    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают

    }
    return render(request, template, context)


#  Страница с постами  (http://127.0.0.1:8000/group/any_slug/)
#  Знаю, знаю, зря создал новый шаблон, хотел попробывать =)

def group_posts(request, slug):
    template = 'posts/group_posts.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        # 'text': 'Здесь будет информация о группах проекта Yatube',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)

#  def group_posts(request, slug):
#    return HttpResponse(f'Страница с постом после фильтра по группе')


# Страница с биографией    (http://127.0.0.1:8000/group_list/)

def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)
