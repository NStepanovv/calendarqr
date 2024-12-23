from django.shortcuts import render
from django.utils.timezone import now
from .models import Video

def home(request):
    available_videos = Video.objects.filter(access_date__lte=now()).exclude(week_number=99).order_by('access_date')
    return render(request, 'main/home.html', {'videos': available_videos})

def video_page(request, week_number):
    video = Video.objects.filter(week_number=week_number).first()
    if not video or video.access_date > now():
        return render(request, 'main/not_available.html', {'video': video})
    return render(request, 'main/video.html', {'video': video})

def not_available(request):
    latest_video = Video.objects.filter(
        access_date__lte=now()
    ).order_by('-access_date').first()

    context = {
        'latest_week': latest_video.week_number if latest_video else None,
    }
    return render(request, 'main/not_available.html', context)