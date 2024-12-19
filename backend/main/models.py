from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название видео")
    file = models.FileField(upload_to='videos/', verbose_name="Файл видео")
    access_date = models.DateTimeField(verbose_name="Дата доступа к видео")
    week_number = models.PositiveIntegerField(unique=True, verbose_name="Номер недели (URL)")

    def __str__(self):
        return self.title
