from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


    #CREATE A STRING FUNCTION TO DISPLAY THE DATA
    def __str__(self):
        return f"{self.title} | Author: {self.author} | Publication year: {self.publication_year}"