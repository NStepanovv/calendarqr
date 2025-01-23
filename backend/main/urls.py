from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('video/<int:week_number>/', views.video_page, name='video_page'),
    path('not-available/', views.not_available, name='not_available'),
]