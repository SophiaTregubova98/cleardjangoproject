from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category
from .parser import parse



def index(request):
    news = News.objects.all()
    categories = Category.objects .all()
    context = {'news': news,
               'title': 'Список новостей:',
               'categories': categories, }
    return render(request,
                  template_name='news/index.html',
                  context=context)
# Render принимает 3 обязательных параметра: request, html документ, словарь в котором ключами будут переменные, которые будут доступны в шаблонах, значения - их значение.
# Если контекста слишком много, создается переменная со словарем context.
# print(dir(request) -  содержит словарь с пользоветльскими данными.

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)
    return render(request, 'news/category.html',
                  {'news': news,
                   'categories': categories,
                   'category': category},
                  )