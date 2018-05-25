from django.db import models


# Model containing bylaws pdf
class Bylaw(models.Model):
    bylaws = models.FileField()


# Model containing policies pdf
class Policy(models.Model):
    policies = models.FileField()


# Model representing projectionists
class Projectionist(models.Model):
    name = models.CharField(max_length=200)


# Model to represent officers
class Officers(models.Model):
    chair = models.CharField(max_length=200)
    fnc = models.CharField(max_length=200)
    snc = models.CharField(max_length=200)
    mw = models.CharField(max_length=200)
    rep = models.CharField(max_length=200)
    pub = models.CharField(max_length=200)
    web = models.CharField(max_length=200)
    projectionists = models.ManyToManyField(Projectionist)


# Model to represent a movie
class Movie(models.Model):
    title = models.CharField(max_length=200)
    last_shown = models.DateField()

    def __str__(self):
        return self.title


# Model to represent current movie schedule
class Schedule(models.Model):
    movies = models.ManyToManyField(Movie)
