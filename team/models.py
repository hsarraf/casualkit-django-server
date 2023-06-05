import random
import string
import django
from django.db import models


def generate_team_id():
    return ''.join(random.choices(string.ascii_letters, k=12))


class Team(models.Model):
    teamId = models.CharField(max_length=20, default=generate_team_id, unique=True)
    people = models.ManyToManyField('player.Player')

    createDate = models.DateTimeField(default=django.utils.timezone.now)
    log = models.TextField(default='', blank=True)

    def get_people(self):
        return [player.username for player in self.people.all()]

    def get_team_data(self):
        return {
            'teamId': self.teamId,
            'people': self.get_people()
        }
