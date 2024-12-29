from django.db import models

class Holiday(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    country = models.CharField(max_length=5)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.name
