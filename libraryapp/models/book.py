from django.db import models
from .library import Library
from .librarian import Librarian

class Book(models.Model):

    title = models.CharField(max_length=100)
    ISBNnumber = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    YearPublished = models.IntegerField()
    location = models.ForeignKey(Library, on_delete=models.CASCADE)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)

    