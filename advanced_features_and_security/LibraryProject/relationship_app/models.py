from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from django.conf import settings



#AUTHOR MODEL
class Author(models.Model):
    name = models.CharField(max_length=100)

    
#BOOK MODEL
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    
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


#ROLE BASE PERMISSIONS IN DJANGO
ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')
    
    objects = CustomUserManager()

    def __str__(self):
        return self.username
    

class LibraryPermission(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    can_view_books = models.BooleanField(default=False)
    can_create_books = models.BooleanField(default=False)
    can_edit_books = models.BooleanField(default=False)
    can_delete_books = models.BooleanField(default=False)

    def __str__(self):
        return f"Permissions for {self.user.username}"

