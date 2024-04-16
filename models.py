from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/')
    description = models.TextField()
    rating = models.FloatField()
    duration = models.IntegerField()
    genre = models.CharField(max_length=50)
    trailer_url = models.URLField()

    def __str__(self):
        return self.title
