import string
import random
import django
from django.db import models

from team.models import Team


def generate_social_id():
    return ''.join(random.choices(string.ascii_uppercase, k=3)) + '-' +\
           ''.join(random.choices(string.ascii_uppercase, k=5)) + '-' + \
           str(random.randint(100, 999))


def generate_social_id2():
    return ''.join(random.choices(string.ascii_letters, k=16))


class Social(models.Model):
    userId = models.UUIDField(primary_key=True, editable=False)
    username = models.CharField(max_length=50, unique=True)

    socialId = models.CharField(max_length=20, unique=True)
    pendingFriends = models.ManyToManyField('player.Player', blank=True, related_name='player_pendingFriends')
    friends = models.ManyToManyField('player.Player', blank=True, related_name='player_friends')

    teams = models.ManyToManyField(Team, blank=True)

    createDate = models.DateTimeField(default=django.utils.timezone.now)
    log = models.TextField(default='', blank=True)

    def get(self):
        return {
            'socialId': self.socialId,
            'pendingFriends': self.get_pending_friends(),
            'friends': self.get_friends(),
            'teams': self.get_teams()
        }

    def get_pending_friends(self):
        return [player.username for player in self.pendingFriends.all()]

    def get_friends(self):
        return [player.username for player in self.friends.all()]

    def get_teams(self):
        return [team.teamId for team in self.teams.all()]

    def __str__(self):
        return self.username
