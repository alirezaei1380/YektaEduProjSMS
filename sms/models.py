from django.db import models
import datetime

class Info(models.Model):

    body = models.TextField()
    phone = models.IntegerField()
    time = models.DateTimeField(default=datetime.datetime.now())