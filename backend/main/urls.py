from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('video/<int:week_number>/', views.video_page, name='video_page'),  # Страница с видео
    path('not-available/', views.not_available, name='not_available'),  # Страница "Не доступно"
]