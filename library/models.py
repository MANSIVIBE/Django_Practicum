from django.db import models

# создаем модель Book
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.title