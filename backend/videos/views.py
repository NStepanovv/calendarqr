from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from django.http import Http404

class VideoDetailView(APIView):
    def get(self, request, week_number):
        try:
            video = Video.objects.get(week_number=week_number)
            serializer = VideoSerializer(video)
            return Response(serializer.data)
        except Video.DoesNotExist:
            raise Http404("Видео не найдено.")