from django.db import models
from django.conf import settings


class Journey(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)


class DayEntry(models.Model):
    journey = models.ForeignKey(Journey, related_name='day_entries', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField()
    text = models.TextField(null=True, blank=True)


class EntryImage(models.Model):
    image = models.ImageField(upload_to=settings.UPLOAD_TO_MEDIA_IMG)
    lat = models.FloatField()
    lon = models.FloatField()
    day_entry = models.ForeignKey(DayEntry, related_name='images', on_delete=models.CASCADE)

