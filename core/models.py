from django.db import models


class Journey(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True)


class DayEntry(models.Model):
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    date = models.DateField()
    text = models.TextField()


class LocationPoint(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    day_entry = models.ForeignKey(DayEntry, on_delete=models.CASCADE)
