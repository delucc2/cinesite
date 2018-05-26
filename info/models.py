from django.db import models
from datetime import date
from itertools import chain


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


# Returns queryset of ONLY upcoming movies
class UpcomingMovies(models.Manager):
    def get_queryset(self):
        return Movie.movies.filter(showing_date__gte=date.today())


# Model to represent a movie
class Movie(models.Model):
    title = models.CharField(max_length=200, default="Superbad")
    showing_date = models.DateField(default=date.today())
    POSSIBLE_RATINGS = (("G", "G"),
                        ("PG", "PG"),
                        ("PG-13", "PG-13"),
                        ("R", "R"))
    rating = models.CharField(max_length=5,
                              choices=POSSIBLE_RATINGS,
                              default="PG-13")
    runtime = models.IntegerField(default=0)
    director = models.CharField(max_length=200, default="John Cena")
    poster = models.ImageField(upload_to='posters/%Y', default='home/static/home/images/logo.png')
    trailer_src = models.CharField(max_length=1000, default='https://www.youtube.com/embed/jPEYpryMp2s')
    description = models.CharField(max_length=10000, default='A moving picture, for sure')

    movies = models.Manager()
    upcoming_movies = UpcomingMovies()

    def __str__(self):
        return self.title


# Model to represent current movie schedule
class Schedule(models.Model):
    movies = models.ManyToManyField(Movie)
