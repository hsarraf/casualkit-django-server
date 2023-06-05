import django
from django.db import models


Gender = [('male', 'Male'), ('female', 'Female')]


class UserProfile(models.Model):
    userId = models.UUIDField(primary_key=True, editable=False)
    username = models.CharField(max_length=50, unique=True)

    emailAddress = models.EmailField(blank=True)
    displayName = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, default=Gender[0], choices=Gender)
    avatar = models.CharField(max_length=50, blank=True)

    createDate = models.DateTimeField(default=django.utils.timezone.now)
    log = models.TextField(default='', blank=True)

    def get(self):
        return {
            'emailAddress': self.emailAddress,
            'gender': self.gender,
            'displayName': self.displayName,
            'avatar': self.avatar,
        }

    def __str__(self):
        return self.username
