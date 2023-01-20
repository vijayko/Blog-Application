# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from PIL import Image
class CustomUser(AbstractUser): 
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(
        get_user_model(), 
        on_delete=models.CASCADE,
    )
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username 

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 1024 or img.width > 1024:
            new_img = (1024, 1024)
            img.thumbnail(new_img)
            img.save(self.avatar.path)