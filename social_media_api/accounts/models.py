from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Adding Extral Fields
    bio = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_images', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True )

    def __str__(self):
        return self.username