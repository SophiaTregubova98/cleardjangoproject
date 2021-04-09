"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('news/', include('news.urls')),
    path('', admin.site.urls),
]

# path('test/', test) - возможная запись, но неактуальная.
#В актуальной записи:
#news - название приложения, urls - вручную созданная папка с маршрутками конкретного приложения

# Функция path принимает параметры:
#route - маршрут
#views - функция, вид страницы

from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Мы формируем маршрут только в отладочном режиме. По этому маршруту Django будет отдавать медиафайлы.
# Когда debug = False, медиафайлы не будут добавляться по этому адресу
# alt + enter = импорт нужного модуля из нужной библиотеки

