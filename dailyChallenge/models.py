import time
import django
from django.db import models
from .params import *


class DailyChallengeItem(models.Model):
    class TargetType(models.TextChoices):
        WINS = 'Wins',
        FANS = 'Fans',
        POWER = 'Power'

    class RewardType(models.TextChoices):
        FAN = 'Fan',
        COIN = 'Coin',
        GEM = 'Gem'

    index = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    target = models.IntegerField(default=0)
    targetType = models.CharField(max_length=10, choices=TargetType.choices, default=TargetType.WINS)
    reward = models.IntegerField(default=0)
    rewardType = models.CharField(max_length=10, choices=RewardType.choices, default=RewardType.FAN)

    createDate = models.DateTimeField(default=django.utils.timezone.now)

    def get(self):
        return {'index': self.index,
                'name': self.name,
                'description': self.description,
                'target': self.target,
                'targetType': self.targetType,
                'reward': self.reward,
                'rewardType': self.rewardType}

    def __str__(self):
        return self.name


class DailyChallenge(models.Model):
    userId = models.UUIDField(primary_key=True, editable=False)
    username = models.CharField(max_length=50, unique=True)

    nextIndex = models.IntegerField(default=0)
    challenge = models.ForeignKey(DailyChallengeItem, on_delete=models.CASCADE, null=True)
    timestamp = models.IntegerField(default=0)

    createDate = models.DateTimeField(default=django.utils.timezone.now)
    log = models.TextField(default='', blank=True)

    def get(self):
        if time.time() - self.timestamp > DAY_IN_SECONDS:
            try:
                challenge = DailyChallengeItem.objects.get(index=self.nextIndex)
                self.nextIndex += 1
                self.timestamp = time.time()
                self.challenge = challenge
                self.save()
                return challenge.get()
            except DailyChallengeItem.DoesNotExist:
                return None
        else:
            return None

    def __str__(self):
        return self.username
