from django.db import models

# В Django 3 типа связи полей. ManyToMany, OnetoOne, ForeignKey.
# class ForeignKey(to, on_delete, **options). Отношения многие-к-одному.
# class ManyToManyField(to, **options). Отношения многие ко многим.
# class OneToOneField(to, on_delete, parent_link=False, **options). Отношения один - к - одному


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название новости')
    content = models.TextField(blank=True, verbose_name='Текс')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_add = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/$Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        # Изменение названия класса модели в единственном числе
        verbose_name_plural = 'Новости'
        ordering = ['created_at']
        # Сортировка. В списке указываются параметры сортировки по первому, второму и тд полню




class Category(models.Model):
    title = models.CharField(max_length=150,
                             db_index=True,
                             verbose_name='Наименование категорий') #индексирует поле
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        ordering = ['title']




