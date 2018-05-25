from django.db import models


# Model to represent movies shown
class Movie(models.Model):
    title = models.CharField(max_length=200)
    last_shown = models.DateField()

    def __str__(self):
        return self.title


# Model to represent current movie schedule
class Schedule(models.Model):
    movies = models.ManyToManyField(Movie)