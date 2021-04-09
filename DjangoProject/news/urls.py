from django.urls import path
from .views import *

# .views - точка указывает на текущий директорий

urlpatterns = [
    path('category/<int:category_id>/', get_category, name='category'),
    path('', index, name='home')
]