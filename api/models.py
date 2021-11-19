from django.db import models

# Create your models here.
class Event(models.Model):
    #user = models.ForeignKey()
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    