import uuid
import django
from django.db import models

from userProfile.models import UserProfile
from social.models import Social
from score.models import Score
from dailyChallenge.models import DailyChallenge
from store.models import *


class Player(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)

    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    social = models.ForeignKey(Social, on_delete=models.CASCADE, null=True)
    score = models.ForeignKey(Score, on_delete=models.CASCADE, null=True)
    dailyChallenge = models.ForeignKey(DailyChallenge, on_delete=models.CASCADE, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)

    createDate = models.DateTimeField(default=django.utils.timezone.now)
    log = models.TextField(default='', blank=True)

    def get(self):
        return {
            'userId': str(self.userId),
            'username': self.username,
            'profile': None if self.userProfile is None else self.userProfile.get(),
            'social': None if self.social is None else self.social.get(),
            'dailyChallenge': None if self.dailyChallenge is None else self.dailyChallenge.get(),
            'score': None if self.score is None else self.score.get(),
            'store': [item.get() for item in StoreItem.objects.all()],
        }

    def get_info(self):
        return {
            'userId': str(self.userId),
            'username': self.username,
            'emailAddress': self.userProfile.emailAddress,
            'gender': self.userProfile.gender,
            'socialId': self.social.socialId
        }

    def __str__(self):
        return self.username
