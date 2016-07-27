from django.db import models
from django.utils import timezone



class Genre(models.Model):
    name = models.CharField(max_length=75)
    note1 = models.CharField(max_length=100, blank=True)
    note2 = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return '%s' % (self.name)



class Movie(models.Model):
    name = models.CharField(max_length=100, blank=False)
    date = models.DateField(blank=False, default=timezone.now)
    genre= models.ForeignKey(Genre)
    grossing = models.FloatField(blank=False,null=False)
    budget = models.FloatField()
