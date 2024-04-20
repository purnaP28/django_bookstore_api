from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    test_field = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
