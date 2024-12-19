from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import Video

def home(request):
    return render(request, 'main/home.html')

def video_page(request, week_number):
    video = get_object_or_404(Video, week_number=week_number)
    if video.access_date > now():
        return render(request, 'main/not_available.html', {'video': video})
    return render(request, 'main/video.html', {'video': video})

def not_available(request):
    # Получаем последний доступный объект Video
    latest_video = Video.objects.filter(
        access_date__lte=now()
    ).order_by('-access_date').first()  # Убедимся, что выбирается по дате доступа

    context = {
        'latest_week': latest_video.week_number if latest_video else None,
    }
    return render(request, 'main/not_available.html', context)