from email import message
from django.db import models

# Create your models here.

class FeedBack(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField(null=True, blank=True)
    feed = models.TextField(null = True, blank=True)

    def __str__(self) -> str:
        return self.name, self.feed


class Year(models.Model):
    year = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.year

class Song(models.Model):
    name = models.CharField(max_length=200)
    song = models.FileField(upload_to='audio/')
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name



