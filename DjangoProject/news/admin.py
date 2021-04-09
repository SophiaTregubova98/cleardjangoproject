from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_add', 'is_published')
    # Нужно для добавления этих столбцов в админскую панель Новостей
    list_display_links = ('id', 'title')
    # Активные ссылки
    search_fields = ('title', 'content')
    # Возможность поиска. Аргументы - по каким полям поиск.
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
# Регистрация таблицы БД в админке.
admin.site.register(Category, CategoryAdmin)
