from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#AUTHOR MODEL
class Author(models.Model):
    name = models.CharField(max_length=100)

    
#BOOK MODEL
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    
#LIBRARY MODEL
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    
#LIBARIAN MODEL
class Libarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)



#AUTHENTICATION PART
#Create a user


#Retrieve a user base on the username
