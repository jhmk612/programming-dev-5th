from django.db import models

# Create your models here.

class Episode(models.Model):
    title=models.CharField(max_length=50)
    url=models.URLField()

    def __str__(self):
        return self.title