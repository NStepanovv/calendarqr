from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'access_date', 'week_number']
    search_fields = ['title']
    list_filter = ['access_date']