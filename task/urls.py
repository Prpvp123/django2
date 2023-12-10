from django.urls import re_path, path
from . import views

urlpatterns = [
    path('user/<str:login>/<str:directory>/<str:post>', views.user, name='user'),
    re_path('second_index/', views.second_index, name='main'),
    re_path('error/', views.error, name='error'),
]