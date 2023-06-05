import django
from django.db import models


class Score(models.Model):
    userId = models.UUIDField(primary_key=True, editable=False)
    username = models.CharField(max_length=50, unique=True)

    coin = models.IntegerField(default=0)
    gem = models.IntegerField(default=0)
    cup = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    fan = models.IntegerField(default=0)

    createDate = models.DateTimeField(default=django.utils.timezone.now)
    log = models.TextField(default='', blank=True)

    def get(self):
        return {
            'coin': self.coin,
            'gem': self.gem,
            'cup': self.cup,
            'score': self.score,
            'level': self.level,
            'rank': self.rank,
            'xp': self.xp,
            'fan': self.fan
        }

    def __str__(self):
        return self.username
