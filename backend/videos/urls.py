from django.urls import path
from .views import VideoDetailView

urlpatterns = [
    path('videos/<int:week_number>/', VideoDetailView.as_view(), name='video-detail'),
]