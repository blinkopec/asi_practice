from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Report(models.Model):
    id = models.IntegerField(primary_key=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    dateReport = models.DateTimeField(null=True)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.dateReport <= now 


class InputData(models.Model):
    id = models.IntegerField(primary_key=True)
    startTemperature = models.IntegerField(default=0)
    endTemperature = models.IntegerField(default=0)
    thremalCapacity = models.IntegerField(default=0)
    weigth = models.IntegerField(default=0)


class ReportInputData(models.Model):
    id = models.IntegerField(primary_key=True)
    idRerport = models.ForeignKey(Report, on_delete=models.CASCADE)
    idInputData = models.ForeignKey(InputData, on_delete=models.CASCADE)
