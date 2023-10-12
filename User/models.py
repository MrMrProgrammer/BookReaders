from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    profile_photo = models.ImageField(upload_to='user_profile')
    nickname = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email_active_code = models.CharField(max_length=100, null=True, blank=True)
    page_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'User'
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'